from typing import Any
from django.views.generic import TemplateView
import random
from main.constants import (
    WELCOME_MESSAGE_INTRO,
    WELCOME_MESSAGE_CUQI,
    WELCOME_MESSAGE_BODY,
)


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        welcome_message_intro = self._get_random_welcome_message(WELCOME_MESSAGE_INTRO)
        welcome_message_cuqi = self._get_random_welcome_message(WELCOME_MESSAGE_CUQI)
        welcome_message_body = self._get_random_welcome_message(WELCOME_MESSAGE_BODY)

        if "---" in welcome_message_intro:
            welcome_message_intro = welcome_message_intro.replace(
                "---", welcome_message_cuqi
            )
            welcome_message_cuqi = ""

        context["welcome_message_intro"] = welcome_message_intro
        context["welcome_message_cuqi"] = welcome_message_cuqi
        context["welcome_message_body"] = welcome_message_body
        context["pre_estim_list"] = self._generate_pre_estim()
        return context

    def _get_random_welcome_message(self, welcome_message_list):
        try:
            index = random.randint(0, len(welcome_message_list) - 1)
            return welcome_message_list[index]
        except Exception:
            return ""

    def _generate_pre_estim(self):
        possibilities = ["super", "mega", "duper", "cruker"]

        pre_estim_list = ""
        total_e = random.randint(2, 10)
        for i in range(total_e):
            index = random.randint(0, len(possibilities) - 1)
            pre_estim_list += f" {possibilities[index]}"

        return pre_estim_list
