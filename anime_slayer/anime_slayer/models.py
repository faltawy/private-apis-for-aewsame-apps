from __future__ import annotations

from typing import Any, List

from pydantic import BaseModel


class MetaData(BaseModel):
    _limit: str
    _offset: str


class AnimeModel(BaseModel):
    anime_id: str
    anime_name: str
    anime_type: str
    anime_status: str
    anime_season: str
    anime_release_year: str
    anime_age_rating: str
    anime_rating: str
    anime_rating_user_count: str
    anime_description: str
    anime_cover_image: str
    anime_cover_image_full: str
    anime_banner_image: str
    anime_trailer_url: str
    anime_english_title: str
    anime_keywords: str
    allow_comment: str
    anime_updated_at: str
    anime_created_at: str
    anime_genre_ids: str
    anime_genres: str
    anime_release_day: str
    anime_cover_image_url: str
    anime_cover_image_full_url: str
    anime_banner_image_url: str
    anime_updated_at_format: str
    anime_created_at_format: str
    related_animes: List
    related_news: List
    role: str
