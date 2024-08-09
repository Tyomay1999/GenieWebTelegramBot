from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler
from util import *

async def start (update, context):
    text = load_message("main")


    await send_photo(update,context,"main")
    await send_text(update, context,text)
    await send_text_buttons(update,context, "At GenieWeb, we are more than just a web company - were your strategic partners in navigating the digital landscape. With a focus on innovation, creativity, and reliability, we deliver tailored digital solutions that exceed expectations. Join us and experience the difference with GenieWeb.",{
        "start":"Services",
        "stop":"Courses"
    })
    await show_main_menu(update, context, {
        "/start ": "bot main menu ",
        "/website ": "https://genieweb.org/ 😎 ",
        "/services ": "https://genieweb.org/services ",
        "/courses ": "https://genieweb.org/courses ",
        "/linkedin ": "https://www.linkedin.com/company/genieweb/posts/?feedView=all 🔥  ",
        "/upwork": "https://www.upwork.com/agencies/1782759227174416384/",
        "/help ": "Email info@genieweb.org, Phone +374 ( 43 ) 283-000," + "loc: Bashinjagyan 2str 1app 33"

    })

async def website(update,context):
    await send_text(update,context, " Here is our website, welcome https://genieweb.org/  ")

async def services(update,context):
    services = load_message("services")
    await send_text(update,context, services)


async def courses(update,context):
    courses = load_message("courses")
    await send_text(update,context,courses)

async def linkedin(update,context):
    await send_text(update,context, " Here is our linkedin, welcome https://www.linkedin.com/company/genieweb/posts/?feedView=all   ")

async def upwork(update,context):
    await send_text(update,context, " Here is our upwork, welcome https://www.upwork.com/agencies/1782759227174416384/ ")

async def help(update,context):
    help = load_message("help")
    await send_text(update,context, help)

async def hello(update, context):
    # await send_photo(update,context,"main")
    await send_text(update,context,"o Hi, welcome our bot. You can click on the /start word and the bot will be activated")

async def hello_button(update, context):
    services = load_message("services")
    courses = load_message("courses")
    query = update.callback_query.data
    if query == "start":
        await send_text(update, context, services)
    else:
        await send_text(update,context, courses)

# 7200697285:AAFf0V35CDWFgPVwEQ_9Bv3g7dFbpMtcQXQ

app = ApplicationBuilder().token("7200697285:AAFf0V35CDWFgPVwEQ_9Bv3g7dFbpMtcQXQ").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("website", website))
app.add_handler(CommandHandler("services",services))
app.add_handler(CommandHandler("courses", courses))

app.add_handler(CommandHandler("linkedin", linkedin))

app.add_handler(CommandHandler("upwork", upwork))
app.add_handler(CommandHandler("help", help))



app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))
app.add_handler(CallbackQueryHandler(hello_button))


app.run_polling()