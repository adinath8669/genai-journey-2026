import pytest
from services.pdf_service import load_pdf


def test_load_pdf_raises_value_error_for_nonexistent_file():
    """
    A path that doesn't exist should fail to open,
    and load_pdf should translate that into a ValueError
    (not let the raw PdfReader exception leak out).
    """
    with pytest.raises(ValueError):
        load_pdf("this_file_does_not_exist.pdf")


def test_load_pdf_raises_value_error_for_non_pdf_file(tmp_path):
    """
    A file that exists but isn't a real PDF (e.g. a text file
    renamed to .pdf) should also fail to open and raise ValueError.
    """
    fake_pdf = tmp_path / "fake.pdf"
    fake_pdf.write_text("this is not actually a pdf file")

    with pytest.raises(ValueError):
        load_pdf(str(fake_pdf))


def test_load_pdf_raises_value_error_for_insufficient_text(monkeypatch):
    """
    Simulate a scanned/image-only PDF: PdfReader opens fine,
    but every page returns no extractable text. load_pdf should
    raise ValueError because the total text is below
    MIN_RESUME_TEXT_LENGTH.
    """
    class FakePage:
        def extract_text(self):
            return ""  # simulates a scanned page with no text layer

    class FakeReader:
        def __init__(self, path):
            self.pages = [FakePage(), FakePage()]

    monkeypatch.setattr("services.pdf_service.PdfReader", FakeReader)

    with pytest.raises(ValueError):
        load_pdf("irrelevant_path.pdf")


def test_load_pdf_succeeds_with_sufficient_text(monkeypatch):
    """
    Happy path: PdfReader opens fine and pages contain enough
    text — load_pdf should return the extracted, stripped text.
    """
    long_text = "This is a resume with plenty of real content. " * 5

    class FakePage:
        def extract_text(self):
            return long_text

    class FakeReader:
        def __init__(self, path):
            self.pages = [FakePage()]

    monkeypatch.setattr("services.pdf_service.PdfReader", FakeReader)

    result = load_pdf("irrelevant_path.pdf")

    assert result == long_text.strip()