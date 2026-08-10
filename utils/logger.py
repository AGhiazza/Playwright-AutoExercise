import logging
import pathlib
from datetime import datetime

logs_dir = pathlib.Path("reports/logs") 
logs_dir.mkdir(exist_ok=True, parents=True)   #Creates the folder in case it doesn't exist yet.

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")    #Using YYYY-MM-DD ISO

logging.basicConfig(    
    encoding="utf-8",
    filename= logs_dir / f"log_{timestamp}.log",
    level=logging.INFO, 
    format= "%(asctime)s %(levelname)s %(name)s - %(message)s",
    force=True  #Forces this new config if there's an existing one.
)

logger = logging.getLogger("Playwright-AutoExercise")