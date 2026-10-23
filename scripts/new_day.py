"""Create a dated learning note and refresh its index, without overwriting notes."""
from pathlib import Path
from datetime import datetime, date
from zoneinfo import ZoneInfo
import argparse

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--date', type=date.fromisoformat,
                        default=datetime.now(ZoneInfo('Asia/Kolkata')).date(),
                        help='Optional ISO date, YYYY-MM-DD')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    logdir = root/'logs'/f'{args.date:%Y}'/f'{args.date:%m}'
    logdir.mkdir(parents=True, exist_ok=True)
    target = logdir/f'{args.date.isoformat()}.md'
    template = (root/'templates/daily.md').read_text(encoding='utf-8')
    try:
        with target.open('x', encoding='utf-8') as f:
            f.write(template.replace('{date}', args.date.isoformat()))
        print(f'Created {target.relative_to(root)}')
    except FileExistsError:
        print(f'Preserved existing note: {target.relative_to(root)}')
    links=[]
    for p in sorted((root/'logs').glob('*/*/*.md'), reverse=True):
        links.append(f'- [{p.stem}]({p.relative_to(root/"logs").as_posix()})')
    (root/'logs/README.md').write_text('# Learning log\n\n'+'\n'.join(links)+'\n', encoding='utf-8')

if __name__ == '__main__':
    main()
