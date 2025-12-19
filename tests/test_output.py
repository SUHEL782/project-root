import subprocess


def run_script():
    result = subprocess.run(
        ["bash", "analyze_logs.sh"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def test_exact_output():
    """Validates exact output ordering and formatting."""
    expected = """4 10.0.0.1
3 10.0.0.2
3 10.0.0.3"""
    assert run_script() == expected


def test_no_extra_lines():
    """Ensures no extra whitespace or lines are printed."""
    output = run_script().splitlines()
    assert len(output) == 3


def test_numeric_sorting():
    """Ensures sorting is numeric, not lexicographic."""
    counts = [int(line.split()[0]) for line in run_script().splitlines()]
    assert counts == sorted(counts, reverse=True)

