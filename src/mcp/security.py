"""
MCP Security Implementation

This module handles authentication, authorization, and security
for the Model Context Protocol.
"""

import hashlib
import hmac
import logging
import secrets
from typing import Dict, Optional, Any
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class SecurityConfig(BaseModel):
    """Configuration for security settings."""
    enable_auth: bool = True
    secret_key: Optional[str] = None
    token_expiry: int = 3600  # 1 hour
    max_attempts: int = 5


class MCPSecurity:
    """Handles MCP security and authentication."""
    
    def __init__(self, config: SecurityConfig):
        self.config = config
        self.secret_key = config.secret_key or secrets.token_hex(32)
        self.active_tokens: Dict[str, Dict[str, Any]] = {}
        
    def generate_token(self, user_id: str, permissions: Optional[list] = None) -> str:
        """Generate an authentication token."""
        token = secrets.token_hex(32)
        self.active_tokens[token] = {
            "user_id": user_id,
            "permissions": permissions or [],
            "created_at": self._get_timestamp()
        }
        return token
        
    def validate_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Validate an authentication token."""
        if token not in self.active_tokens:
            return None
            
        token_data = self.active_tokens[token]
        if self._is_token_expired(token_data):
            del self.active_tokens[token]
            return None
            
        return token_data
        
    def revoke_token(self, token: str) -> bool:
        """Revoke an authentication token."""
        if token in self.active_tokens:
            del self.active_tokens[token]
            return True
        return False
        
    def check_permission(self, token: str, permission: str) -> bool:
        """Check if a token has a specific permission."""
        token_data = self.validate_token(token)
        if not token_data:
            return False
            
        return permission in token_data.get("permissions", [])
        
    def _get_timestamp(self) -> int:
        """Get current timestamp."""
        import time
        return int(time.time())
        
    def _is_token_expired(self, token_data: Dict[str, Any]) -> bool:
        """Check if a token is expired."""
        current_time = self._get_timestamp()
        created_at = token_data.get("created_at", 0)
        return (current_time - created_at) > self.config.token_expiry 
