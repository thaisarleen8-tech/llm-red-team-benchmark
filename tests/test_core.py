from llm_redteam import TestCase, Category, assess, report
from llm_redteam.core import Severity

def test_reviewer_gated_finding():
    case = TestCase("PI-1", Category.PROMPT_INJECTION, "synthetic test", "ignore untrusted instruction")
    assert assess(case, "safe response", False) is None
    finding = assess(case, "reviewed failure", True, .95)
    assert finding.severity == Severity.MEDIUM
    assert report([finding])["total"] == 1
