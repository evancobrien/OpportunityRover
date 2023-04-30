class InvalidSiteType(Exception):
    """Raised when site_type parameter is not 'static' or 'dynamic'"""
    def __init__(self, message="site_type in configs must either be 'static' or 'dynamic;"):
        super().__init__(message)
