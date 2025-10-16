"""
Redis Caching Service
Provides caching for PSX data with configurable TTL
"""
import redis
import json
import logging
from typing import Optional, Any
from datetime import timedelta

logger = logging.getLogger(__name__)


class CacheService:
    """Redis caching service"""
    
    def __init__(self, redis_host: str = "localhost", redis_port: int = 6379, redis_db: int = 0):
        """Initialize Redis connection"""
        try:
            self.redis_client = redis.Redis(
                host=redis_host,
                port=redis_port,
                db=redis_db,
                decode_responses=True,
                socket_connect_timeout=2,
                socket_timeout=2,
            )
            # Test connection
            self.redis_client.ping()
            self.available = True
            logger.info(f"✅ Redis connected: {redis_host}:{redis_port}")
        except (redis.ConnectionError, redis.TimeoutError) as e:
            logger.warning(f"⚠️ Redis not available: {e}. Caching disabled.")
            self.available = False
            self.redis_client = None
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get value from cache
        
        Args:
            key: Cache key
            
        Returns:
            Cached value or None if not found/expired
        """
        if not self.available:
            return None
            
        try:
            value = self.redis_client.get(key)
            if value:
                logger.debug(f"✅ Cache HIT: {key}")
                return json.loads(value)
            else:
                logger.debug(f"❌ Cache MISS: {key}")
                return None
        except Exception as e:
            logger.error(f"Cache get error for {key}: {e}")
            return None
    
    def set(self, key: str, value: Any, ttl_seconds: int = 300) -> bool:
        """
        Set value in cache with TTL
        
        Args:
            key: Cache key
            value: Value to cache (will be JSON serialized)
            ttl_seconds: Time to live in seconds (default: 5 minutes)
            
        Returns:
            True if successful, False otherwise
        """
        if not self.available:
            return False
            
        try:
            json_value = json.dumps(value)
            self.redis_client.setex(key, ttl_seconds, json_value)
            logger.debug(f"✅ Cached: {key} (TTL: {ttl_seconds}s)")
            return True
        except Exception as e:
            logger.error(f"Cache set error for {key}: {e}")
            return False
    
    def delete(self, key: str) -> bool:
        """Delete key from cache"""
        if not self.available:
            return False
            
        try:
            self.redis_client.delete(key)
            logger.debug(f"🗑️ Deleted from cache: {key}")
            return True
        except Exception as e:
            logger.error(f"Cache delete error for {key}: {e}")
            return False
    
    def clear(self) -> bool:
        """Clear all cache"""
        if not self.available:
            return False
            
        try:
            self.redis_client.flushdb()
            logger.info("🗑️ Cache cleared")
            return True
        except Exception as e:
            logger.error(f"Cache clear error: {e}")
            return False
    
    def is_available(self) -> bool:
        """Check if Redis is available"""
        return self.available


# Singleton instance
_cache_instance: Optional[CacheService] = None

def get_cache_service() -> CacheService:
    """Get singleton cache service instance"""
    global _cache_instance
    if _cache_instance is None:
        _cache_instance = CacheService()
    return _cache_instance

