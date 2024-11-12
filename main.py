from services.html_content_extractor import HtmlContentExtractor
from services.schedule_content_transformer import ScheduleContentTransformer
from helpers.json_handler import JsonHandler

URL = "https://plan.ue.wroc.pl/l_pozycjaplanu1.php?se=56&gr=135/1"

rows = HtmlContentExtractor.extract(URL)
schedule = ScheduleContentTransformer.transform(rows)

JsonHandler.load(schedule)