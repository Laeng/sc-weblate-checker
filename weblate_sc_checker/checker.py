from django.utils.translation import gettext_lazy
from weblate.checks.base import TargetCheck
import re

class SCVariableCheck(TargetCheck):
    # Used as identifier for check, should be unique
    # Has to be shorter than 50 characters
    check_id = "SCVariable"

    # Short name used to display failing check
    name = gettext_lazy("StarCitizen Variable Format check")

    # Description for failing check
    description = gettext_lazy("Variable Format is not matched with source text")

    # Real check code
    def check_single(self, source, target, unit):
        variableExpr = re.compile(r"\~[a-zA-Z]+\([^\)]*\)")
        return set(variableExpr.findall(source)) != set(variableExpr.findall(target))


class SCParameterCheck(TargetCheck):
    # Used as identifier for check, should be unique
    # Has to be shorter than 50 characters
    check_id = "SCParameter"

    # Short name used to display failing check
    name = gettext_lazy("StarCitizen Parameter Format check")

    # Description for failing check
    description = gettext_lazy("Parameter Format is not matched with source text")

    # Real check code
    def check_single(self, source, target, unit):
        parameterExpr = re.compile(r"%ls|%s|%S|%i|%I|%u|%d|%[0-9.]*f|%\.\*f")
        return parameterExpr.findall(source) != parameterExpr.findall(target)