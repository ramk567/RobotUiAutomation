import os
import yaml
from pathlib import Path

class Config:
    """Configuration management for the test framework"""

    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.config_file = self.project_root / "config" / "environments.yaml"
        self.environment = os.getenv("TEST_ENV", "dev")
        self.config_data = self._load_config()

    def _load_config(self):
        """Load configuration from YAML file"""
        try:
            with open(self.config_file, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")

    def get_base_url(self):
        """Get base URL for current environment"""
        return self.config_data[self.environment]["base_url"]

    def get_browser(self):
        """Get browser configuration"""
        return self.config_data[self.environment].get("browser", "chrome")

    def get_timeout(self):
        """Get default timeout"""
        return self.config_data[self.environment].get("timeout", 10)

    def get_database_config(self):
        """Get database configuration"""
        return self.config_data[self.environment].get("database", {})

    def get_api_config(self):
        """Get API configuration"""
        return self.config_data[self.environment].get("api", {})

# Global config instance
config = Config()
