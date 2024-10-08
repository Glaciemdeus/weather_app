from loguru import logger


# Для сохранения логов 
logger.add(
			"log/data/debug.log",
			format="{time} {level} {message}",
			level="DEBUG",
			rotation="10 KB",
			compression="zip"
		)