import random
import string

from .models import URL
from .extensions import db


class ShortenerService:
    @staticmethod
    def generate_random_code(length=6):
        """Generates a random alphanumeric string of a given length."""
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(length))

    @staticmethod
    def create_short_url(original_url, custom_alias=None):
        """Creates a new URL mapping and returns (URL object, error_message)."""

        code_to_use = custom_alias if custom_alias else None

        if code_to_use:
            existing = URL.query.filter_by(short_code=code_to_use).first()
            if existing:
                return None, "This custom alias is already taken."
        else:
            attempts = 0
            while attempts < 10:
                code_to_use = ShortenerService.generate_random_code()
                if not URL.query.filter_by(short_code=code_to_use).first():
                    break
                attempts += 1
            else:
                return None, "Could not generate a unique code. Please try again."

        new_url = URL(  # type: ignore[call-arg]
            original_url=original_url,
            short_code=code_to_use,
            custom_alias=custom_alias,
        )

        try:
            db.session.add(new_url)
            db.session.flush()
            db.session.commit()
            db.session.refresh(new_url)
            return new_url, None
        except Exception as e:
            db.session.rollback()
            import traceback

            traceback.print_exc()
            return None, f"Database error: {str(e)}"

    @staticmethod
    def get_all_urls():
        return URL.query.order_by(URL.created_at.desc()).all()

    @staticmethod
    def get_url_stats():
        total_links = URL.query.count()
        total_clicks = db.session.query(db.func.sum(URL.clicks)).scalar() or 0
        top_links = URL.query.order_by(URL.clicks.desc()).limit(5).all()
        return {
            "total_links": total_links,
            "total_clicks": total_clicks,
            "top_links": top_links,
        }

    @staticmethod
    def delete_url(url_id):
        url = URL.query.get(url_id)
        if url:
            db.session.delete(url)
            db.session.commit()
            return True
        return False
