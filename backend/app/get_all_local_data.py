import logging

from services.db.retrieve_all_data_from_repos import get_all_repo_data
from services.sqlite import SQLiteDatabase
from utils.exceptions import NoDataOnRepoDatabase


async def add_repo_to_db(db: SQLiteDatabase):
    # execution
    logging.debug(db)
    try:
        result = await get_all_repo_data(db=db)
        return result
    except NoDataOnRepoDatabase:
        logging.error("EXCEPTION FOUND: No data was found on 'repositories' table")
        return None
    except Exception as e:
        logging.error(f"EXCEPTION FOUND: {e}")
        return None
