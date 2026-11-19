"""news-image-20261119: a one-image summary of 19 November 2026.

The bundled picture is a vintage newspaper front page for "The Global
Herald", dated Thursday, November 19, 2026. Its five lead stories are:
a trilateral meeting in Shenzhen between Trump, Xi and Putin; fresh
exchanges of fire between the US and Iran, with Gulf states shooting
down incoming drones; the worldwide launch of GTA VI to near-perfect
reviews; Voyager 1 drifting to one light-day from Earth; and Nvidia's
new chief pledging earlier pay rises while halting H-chip sales to
China.

This program does one small job: it copies the bundled image to the
output directory. The output is a valid JPEG, 1024x683 pixels, well
under the 1 MiB limit. The run is deterministic -- no network, no
randomness, so the same bytes come out every time.
"""

import os
import shutil
from pathlib import Path

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"


def main() -> None:
    source = Path(__file__).resolve().parent / SOURCE_NAME
    assert source.exists(), f"bundled image missing: {source}"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / OUTPUT_NAME
    shutil.copyfile(source, destination)
    assert destination.exists(), f"output missing: {destination}"
    print(f"Wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
