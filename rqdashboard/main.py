import os

from flask import Flask
import rq_dashboard

app = Flask(__name__)
app.config.from_object(rq_dashboard.default_settings)
redis_url = os.environ.get('RQ_DASHBOARD_REDIS_URL')
if not redis_url:
    raise ValueError('RQ_DASHBOARD_REDIS_URL environment variable is not set')
app.config["RQ_DASHBOARD_REDIS_URL"] = redis_url
rq_dashboard.web.setup_rq_connection(app)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

if __name__ == "__main__":
    app.run()
