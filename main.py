import config
import logging

from aiogram import Bot, Dispetcher, executor, types

#log
logging.basicConfig(level=logging.INFO)

#init
bot = Bot(token=config.Token)
dp = Dispetcher (bot)

# echo
@dp.massege_hendler()
async def echo(massege: types.MAssege):
  await massage.answer(massege.text)

  #run long-polling
  if __name__ := "__main__":
    executor.start_polling(dp, skip_updates =False)
