from app.core.helper import create_app
from app.core.db import db
from app.home.views import home_views

# Development Config
config = 'app.config'
# Production Config
# config = 'config.Prod'

app = create_app(config)
db.init_app(app)

# register blueprint
app.register_blueprint(home_views)
