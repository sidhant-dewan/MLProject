    try:
        a= 1/0
    except Exception as e:
        logging.info("D")
        raise CustomException(e,sys)