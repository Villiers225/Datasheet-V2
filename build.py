#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT/'data/content.json'
TEMPLATE = ROOT/'template.html'
OUT = ROOT/'index.html'

def svg_bar(items, unit='', width=360, bar_h=16, gap=6, pad=10):
    if items:
        maxv = max(v for _,v in items) * 1.1
    else:
        maxv = 1
    h = pad*2 + len(items)*(bar_h+gap)-gap
    y = pad
    parts = []
    parts.append('<svg viewBox="0 0 %d %d" role="img" aria-label="exhibit">' % (width, h))
    for label, val in items:
        w = int((val/maxv)*(width-120))
        parts.append('<text x="0" y="%d" class="label">%s</text>' % (y+bar_h-3, str(label)))
        parts.append('<rect x="110" y="%d" width="%d" height="%d" class="bar"/>' % (y, w, bar_h))
        val_txt = ("%g%s" % (val, unit)) if unit else ("%g" % (val))
        parts.append('<text x="%d" y="%d" class="value">%s</text>' % (110+w+4, y+bar_h-3, val_txt))
        y += bar_h+gap
    parts.append('</svg>')
    return ''.join(parts)

def html_escape(s):
    return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def render_box(box):
    verb_items = ''.join("<li>%s</li>" % html_escape(v) for v in box.get('verbatim', []))
    verb = "<ul>%s</ul>" % verb_items
    ex_blocks = []
    for ex in box.get('exhibits', []):
        svg = ''
        if ex.get('type') == 'bar':
            svg = svg_bar(ex.get('items', []), unit=ex.get('unit',''))
        fig = ("<li><span class='chip'>%s</span> %s %s"
               "<figure class='panel' style='margin-top:8px'>%s</figure></li>") % (
                    html_escape(ex.get('id','Ex.')),
                    html_escape(ex.get('title','')),
                    html_escape(ex.get('source_ref','')),
                    svg
               )
        ex_blocks.append(fig)
    exhibits = "<ul>%s</ul>" % ''.join(ex_blocks)
    return ("<section class='box'><h2>%s</h2>"
            "<div class='two'>"
            "<div class='panel'><h3>Verbatim (from PDF)</h3>%s</div>"
            "<div class='panel'><h3>Evidence & Exhibits</h3>%s</div>"
            "</div></section>") % (
                html_escape(box.get('heading','')),
                verb,
                exhibits
            )

def main():
    data = json.loads(DATA.read_text(encoding='utf-8'))
    boxes_html = ''.join(render_box(b) for b in data.get('boxes', []))
    refs_html = ''.join("<li>%s</li>" % html_escape(r) for r in data.get('references', []))
    tmpl = TEMPLATE.read_text(encoding='utf-8')
    out = (tmpl
           .replace('{{title}}', data.get('title',''))
           .replace('{{updated}}', data.get('updated',''))
           .replace('{{boxes}}', boxes_html)
           .replace('{{references}}', refs_html))
    OUT.write_text(out, encoding='utf-8')
    print('Built', OUT)

if __name__ == '__main__':
    main()
