module.exports = {
    apps: [
        {
            name: "gunicorn",
            script: "poetry run gunicorn -w 8 -b 0.0.0.0:8000 kanban_life.wsgi"
        }
    ]
}
