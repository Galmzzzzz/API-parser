from parser import parser


class ParserService:
    def get_data(self):
        return parser()

    def parse_data(self):
        parser()
        return {"status": "success"}