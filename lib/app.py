import os
import subprocess
import router
import utils

class ShmupMate:
    def __init__(self):
        config_path = "data/config.json"
        if not os.path.exists(config_path):
            print("Initializing...")
            subprocess.run(["python", "lib/seed.py"], check=True)

        self.config = utils.load_json(config_path)

if __name__ == "__main__":
    app = ShmupMate()
    r = router.Router(app.config)
    r.run()
