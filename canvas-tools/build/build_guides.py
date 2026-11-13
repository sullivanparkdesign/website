"""Resources page (Journal.dc.html) and the five guides, built from one template.
Guide 01 lives in Article.dc.html; guides 02 to 05 are new pages cloned from it.
Run: python3 build/build_guides.py canvas/project   (then nav_upgrade.py)"""
import json, os, re, sys

ROOT = sys.argv[1]
HERE = os.path.dirname(__file__)
def blobs(d): return json.load(open(os.path.join(HERE, '..', d, 'blobs.json')))
LB, CB, SB, RB, HB = blobs('laura'), blobs('callum'), blobs('smash'), blobs('rooster'), blobs('hr')

SERIF = "'Cormorant Infant', Garamond, serif"
TEAL, INK, BODY, MUTED = '#4E6368', '#121414', '#1F2426', '#4E5558'
ARROW = '<svg width="22" height="10" viewBox="0 0 26 10" fill="none" aria-hidden="true"><path d="M0 5h24M20 1l4 4-4 4" stroke="currentColor" stroke-width="1.1"></path></svg>'
WRAP = 'width: 100%; max-width: 1680px; margin: 0 auto'
GUTTER = 'clamp(20px, 5vw, 72px)'
PALM = '<img class="sp-sway" src="/_blob/fddc24a18e2595d21f63da9f1d7bf0d5" alt="" width="1800" height="1200" style="position: absolute; top: -20px; right: -20px; width: min(1320px, 110vw); height: auto; max-width: none; opacity: 0.16; mix-blend-mode: multiply; pointer-events: none; z-index: 0">'

CASES = {
    'laura': ('Party-With-Laura.dc.html', '/_blob/' + LB['hero-desk'], 'Squarespace · Art Studio', 'pARTy With Laura', 'The pARTy With Laura homepage'),
    'callum': ('Callum-Frost.dc.html', '/_blob/' + CB['hero-desk'], 'Squarespace · Actor', 'Callum Frost', 'The Callum Frost homepage'),
    'smash': ('Smash.dc.html', '/_blob/' + SB['hero-desk'], 'Custom-coded · Performing Arts', 'SMASH Performing Arts Studio', 'The SMASH Performing Arts Studio homepage'),
    'rooster': ('Rooster-Den.dc.html', '/_blob/' + RB['hero-desk'], 'Shopify · Online Retail', 'The Rooster Den Co', 'The Rooster Den Co homepage'),
    'hamish': ('Hamish-Ross.dc.html', '/_blob/' + HB['hero-desk'], 'Custom-coded · Real Estate', 'Hamish Ross Real Estate', 'The Hamish Ross Real Estate homepage'),
}


def label(text, color=TEAL, size=15):
    return f'<p style="margin: 0; display: flex; align-items: center; gap: 16px; font-size: {size}px; letter-spacing: 0.2em; text-transform: uppercase; color: {color}"><span aria-hidden="true" style="display: block; width: 40px; height: 1px; background: {color}"></span>{text}</p>'

def A(href, text):
    return f'<a href="{href}" style="color: {TEAL}; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 4px">{text}</a>'

def P(t):
    return f'<p style="margin: 0; font-size: 19px; line-height: 1.8; color: {BODY}">{t}</p>'

def ticks(items):
    lis = ''.join(f'<li style="display: flex; gap: 16px; font-size: 19px; line-height: 1.6; color: {BODY}"><span aria-hidden="true" style="flex: none; width: 18px; height: 1px; margin-top: 15px; background: {TEAL}"></span><span>{x}</span></li>' for x in items)
    return f'<ul style="list-style: none; margin: 4px 0; padding: 0; display: flex; flex-direction: column; gap: 12px">{lis}</ul>'

def figure(img, alt):
    return f'''<figure class="sp-reveal" style="margin: 28px 0 0; position: relative; padding: 0 20px 20px 0">
<span aria-hidden="true" style="position: absolute; top: 20px; left: 20px; right: 0; bottom: 0; border: 1px solid rgba(78, 99, 104, 0.45)"></span>
<div class="sp-photo" style="position: relative"><img src="{img}" alt="{alt}" width="1080" height="720" loading="lazy" style="width: 100%; aspect-ratio: 3 / 2; object-fit: cover"></div>
</figure>'''

def quote(t):
    return f'<blockquote class="sp-reveal" style="margin: 36px 0; padding: clamp(32px, 4vw, 48px) 0; border-top: 1px solid {TEAL}; border-bottom: 1px solid {TEAL}; text-align: center"><p style="margin: 0; font-family: {SERIF}; font-style: italic; font-weight: 300; font-size: clamp(30px, 3.2vw, 46px); line-height: 1.25; color: {INK}; text-wrap: balance">{t}</p></blockquote>'


# ------------------------------------------------------------- special figures
def compare_table():
    rows = ['Best for', 'Everyday updates', 'Selling online', 'Extra features', 'Hosting and security']
    cols = [
        ('Squarespace', ['Service businesses that want a polished site they can update themselves.',
                         'Easy. You can change text, swap photos and add posts yourself.',
                         'Works well for a modest range of products, digital goods or gift cards.',
                         'Built-in tools, plus a range of extensions.',
                         'Included and managed for you.']),
        ('Shopify', ['Online stores that need products, payments and shipping managed in one place.',
                     'Easy for products, collections and store content.',
                     'Built for it, from inventory to checkout.',
                     'A large app store for almost anything a store needs.',
                     'Included and managed for you.']),
        ('Custom-coded', ['Projects that need full design freedom or features beyond a template.',
                          'Depends on how the site is built, so we plan it together first.',
                          'Possible, usually by connecting a dedicated store or payment service.',
                          'Anything you need, such as a members’ portal or an AI assistant.',
                          'Arranged separately, as part of the project.']),
    ]
    cards = ''.join(f'''<div class="gd-cmp-col">
<h3 style="margin: 0; padding-bottom: 14px; border-bottom: 1px solid {TEAL}; font-family: {SERIF}; font-weight: 400; font-size: 28px; line-height: 1.15; color: {INK}">{name}</h3>
<dl style="margin: 0; display: flex; flex-direction: column">{''.join(f'<div style="padding: 14px 0; border-bottom: 1px solid rgba(78, 99, 104, 0.22); display: flex; flex-direction: column; gap: 6px"><dt style="font-size: 13px; letter-spacing: 0.16em; text-transform: uppercase; color: {MUTED}">{r}</dt><dd style="margin: 0; font-size: 17px; line-height: 1.55; color: {BODY}">{v}</dd></div>' for r, v in zip(rows, vals))}</dl>
</div>''' for name, vals in cols)
    return f'<div class="gd-cmp sp-reveal" role="group" aria-label="Squarespace, Shopify and custom-coded websites compared">{cards}</div>'


def anatomy():
    parts = [('Page address', 'partywithlaura.com › weekly-classes', f'font-size: 15px; color: {MUTED}; overflow-wrap: anywhere'),
             ('Page title', 'Weekly Kids Art Classes | Small Group Lessons in Cloverdale', f'font-family: {SERIF}; font-size: 25px; line-height: 1.25; color: #2C4A8A'),
             ('Description', 'Personalized art instruction for kids and teens (ages 6–18). Small class sizes (2–5 students) ensure individual guidance in painting, sketching, and mixed media.', f'font-size: 16px; line-height: 1.6; color: #3B4042')]
    rows = ''.join(f'<div class="gd-anat-row"><span class="gd-anat-lab">{lab}</span><span style="{st}">{val}</span></div>' for lab, val, st in parts)
    return f'''<figure class="sp-reveal" style="margin: 20px 0 8px; display: flex; flex-direction: column; gap: 14px">
<div style="background: #FAFAF8; padding: 12px; box-shadow: 0 24px 60px rgba(18, 28, 30, 0.08)"><div style="border: 1px solid rgba(78, 99, 104, 0.3); padding: clamp(20px, 3vw, 34px); display: flex; flex-direction: column; gap: 14px">{rows}</div></div>
<figcaption style="font-size: 16px; line-height: 1.6; color: {MUTED}">A real page title and description from {A('Party-With-Laura.dc.html', 'pARTy With Laura')}, written around the way local families search.</figcaption>
</figure>'''


# ------------------------------------------------------------------ guide specs
GUIDES = [
dict(
    file='Article.dc.html', key='Article', tag='Planning', short='What to prepare before a website redesign',
    title_main='What to prepare before', title_em='a website redesign',
    summary='The goals, content, photos and logins worth gathering first, so your project starts smoothly.',
    meta_title='What to Prepare Before a Website Redesign | Sullivan Park Design',
    meta_desc='A practical guide from Sullivan Park Design to the goals, content, photos, brand files and logins worth gathering before your website redesign begins.',
    hero=('/_blob/c88afba51f29e1af4a1ad91e130aa1ec', 'An open, light-filled pavilion with a long table, looking out over a calm sea'),
    intro='A website redesign runs more smoothly when a few things are ready before the design work begins. You don’t need everything perfect, and you don’t need to do it alone. But the more of this you can gather, the more of our time goes into the parts that make your site stand out. Here’s what helps most, in the order I’d tackle it.',
    takeaways=['Start with what you want your website to do, not how you want it to look.',
               'Note what’s working on your current site, so the redesign builds on it.',
               'Gather your words, brand files and best photos in one place.',
               'Collect logins for your domain, website and Google tools early.',
               'Share a few websites you like, and say what you like about them.'],
    blocks=[
        ('sec', 'goals', 'Know what you want your website to do',
         P('Before colours and layouts, think about the job your website needs to do. More enquiries? Bookings? Online sales? Fewer emails asking the same questions? Most businesses have one main goal and a few supporting ones, and knowing them shapes every decision that follows, from the pages you need to where each button goes.') +
         P(f'It also helps to know who you most want to reach. A website for {A("Party-With-Laura.dc.html", "parents booking art classes")} needs different things than one for {A("Callum-Frost.dc.html", "agents discovering a new actor")}, even when both are simple and clean.')),
        ('sec', 'current', 'Take stock of your current site',
         P('Make a quick list of what’s working and what isn’t. Which pages do people actually use? What do customers ask you that the site should already answer? What feels out of date, or no longer reflects how you work?') +
         P(f'Those everyday questions are useful. For {A("Party-With-Laura.dc.html", "pARTy With Laura")}, common parent questions (what to wear, what to bring, whether there’s a snack break) became short, expandable answers on each program page.') +
         P('If you have Google Analytics or Search Console, note your most visited pages and the searches that bring people in. Keeping those pages at the same address, or redirecting them properly, means a redesign builds on what you already have instead of starting from zero.')),
        ('quote', 'Start with what you want your website to do, not how you want it to look.'),
        ('sec', 'content', 'Plan your pages and words',
         P('List the pages you think you need and the main thing each one should say. A home page, services, about, contact and a few examples of your work cover most small businesses, but your list might also include programs, a shop, a portfolio or FAQs.') +
         P('Gather the words you already have, even rough notes. Copy you love can stay, and anything that isn’t working can be rewritten. If writing isn’t your favourite thing, tell me. Turning notes into clear, warm copy is something I help with.')),
        ('sec', 'brand', 'Gather your brand files',
         P('Find your logo in the best quality you have. Ideally that’s a vector file (SVG, EPS or PDF) plus a PNG with a transparent background. Add your brand colours, fonts and any brand guidelines you’ve been given.') +
         P(f'If you don’t have a palette or fonts yet, that’s okay. A redesign is a natural time to define them, and {A("Brand-Marketing-Design.dc.html", "brand and marketing design")} is part of what I offer. I don’t design logos, but I can build your colours, typography and imagery around the one you have.')),
        ('figure', '/_blob/87b256f87275018e5bfde23768efc920', 'An open notebook of handwritten plans beside a laptop on a wooden desk'),
        ('sec', 'photos', 'Choose your photos',
         P('Photos shape how a website feels more than almost anything else. Your own photos of your work, your space and yourself build a kind of trust that stock photos can’t. Gather the best ones you have, in the largest size available.') +
         P(f'If you’re planning a photo shoot, plan it with the website in mind. Before {A("Callum-Frost.dc.html", "Callum’s")} headshot session, I gave advice on the kinds of photos I wanted for his site, so the shoot and the design worked together.') +
         P('Stock photos still have a place, especially for mood and atmosphere. Choose ones that feel like your brand rather than ones that could belong to anyone.')),
        ('sec', 'access', 'Collect your logins',
         P('Waiting on logins is one of the easiest ways for a project to stall, so it’s worth gathering access early:') +
         ticks(['Your domain, and where you bought it', 'Your current website platform', 'Google Business Profile, Search Console and Analytics',
                'Your email, if it’s connected to your domain', 'Any booking, payment or newsletter tools you use', 'The social media accounts you’d like linked']) +
         P('You don’t need to send passwords by email. Most of these tools let you add a collaborator instead, which is safer and easy to undo later.')),
        ('sec', 'features', 'List your must-have features',
         P('Think about what your website needs to do behind the scenes. Booking, online sales, gift certificates, a contact form that sorts enquiries, a newsletter sign-up or a private area for clients or families are all possible, but each one affects how the site is built.') +
         P(f'Listing them early helps choose the right platform, since {A("Guide-Platforms.dc.html", "Squarespace, Shopify and custom-coded sites")} each handle them differently. {A("Smash.dc.html", "SMASH")}, for example, needed a portal for families, while {A("Rooster-Den.dc.html", "The Rooster Den Co")} needed a store that’s easy to shop.')),
        ('sec', 'inspiration', 'Collect a few websites you like',
         P('Find two or three websites you love, in any industry, and note what you like about each one: the colours, the photos, how easy it is to find things, how it makes you feel. Sites you don’t like are just as helpful, as long as you can say why.') +
         P('A short list of your main competitors is useful too, so your new site can stand apart from them rather than blend in.')),
        ('sec', 'timing', 'Share your timing',
         P('If your new site needs to be ready for something specific, like registration opening, a new season or a product launch, mention it at the start. It’s much easier to plan around a date we both know about.')),
    ],
    bottom='You don’t need all of this before we talk. A rough idea of your goals and a few links to sites you like is a great place to start, and we can work through the rest together. The more you gather, the more of our time can go into the parts that make your website feel like yours.',
    practice=['laura', 'callum', 'smash'],
),
dict(
    file='Guide-Platforms.dc.html', key='Guide-Platforms', tag='Website Design', short='Squarespace, Shopify or custom-coded: choosing your platform',
    title_main='Squarespace, Shopify or <span style="white-space: nowrap">custom-coded:</span>', title_em='choosing your platform',
    summary='How the three platforms I build on compare, and how to tell which one suits your business.',
    meta_title='Squarespace, Shopify or Custom-Coded: Choosing Your Website Platform | Sullivan Park Design',
    meta_desc='A plain-language guide from Sullivan Park Design to choosing between Squarespace, Shopify and a custom-coded website, based on what your business needs.',
    hero=('/_blob/30877871fc4f79c536971d91a8d2f627', 'Three websites side by side: Callum Frost on Squarespace, The Rooster Den Co on Shopify and SMASH Performing Arts Studio, custom-coded'),
    intro='The platform behind your website shapes what it can do, how easy it is to update and how it grows with you. I build on Squarespace, Shopify and custom code, so I don’t have a favourite to push. The right choice depends on your business. Here’s how the three compare, and the questions that usually point to the right one.',
    takeaways=['Squarespace suits service businesses that want to update their own site.',
               'Shopify suits businesses that sell products online.',
               'Custom code suits projects that need full design freedom or features beyond a template.',
               'Think about who will update the site, and how often.',
               'Choose for where your business is heading, not only where it is today.'],
    blocks=[
        ('sec', 'glance', 'The three platforms at a glance',
         P('Each platform is a good choice for the right business. Here’s the short version:') + compare_table()),
        ('quote', 'The right platform is the one that fits how your business works, not the one with the longest feature list.'),
        ('sec', 'squarespace', 'When Squarespace is the right fit',
         P('Squarespace is a great home for service businesses, studios and creatives who want a website that looks polished and stays easy to manage. Hosting, security and updates are handled for you, and everyday changes like editing text, swapping photos or adding a blog post don’t need a designer.') +
         P(f'It also handles more than people expect. {A("Party-With-Laura.dc.html", "pARTy With Laura")} uses it for program pages, booking requests and digital gift certificates, while {A("Callum-Frost.dc.html", "Callum Frost’s")} site keeps things simple with headshots, a resume and media.') +
         P('Where it can feel limiting is with highly unusual layouts or features it wasn’t designed for. Some of those can be added with code or extensions, but if they’re central to your business, it’s worth looking at custom code.')),
        ('sec', 'shopify', 'When Shopify is the right fit',
         P('If selling products is at the heart of your business, Shopify is built for it. Products, inventory, payments, shipping and orders all live in one system, and there’s an app for almost any extra feature a store might need.') +
         P(f'{A("Rooster-Den.dc.html", "The Rooster Den Co")} is a good example. The redesign focused on making the store easier to shop, page by page, while the day-to-day running of the business stayed in one place.') +
         P('Apps can add monthly costs, so it’s worth choosing them carefully. And if your business is mostly services with only a few products, Squarespace may be the simpler choice.')),
        ('sec', 'custom', 'When custom code is the right fit',
         P('A custom-coded website is built from the ground up for your business. It makes sense when you need complete design freedom, a feature no template offers or a site that brings several tools together.') +
         P(f'{A("Smash.dc.html", "SMASH Performing Arts Studio")} needed a password-protected portal for families and an AI assistant that answers questions about the studio and its programmes. {A("Hamish-Ross.dc.html", "Hamish Ross Real Estate")} needed a high-end, luxury identity carried from page to page. Both are things a custom build does well.') +
         P('The trade-off is that editing depends on how the site is built. Some custom sites include an easy way to update content, and others are updated with help. We decide that together before the build starts, so there are no surprises.')),
        ('sec', 'questions', 'Questions that point to the right platform',
         ticks(['Do you sell products online, or mainly services?', 'Who will update the website, and how often?',
                'Do you need anything a template can’t do, like a portal, an AI assistant or a connection to another system?',
                'How important is complete control over the design?', 'Where do you see your business in a few years?']) +
         P('If you’re not sure about some of these, that’s normal. We’ll talk through the options before deciding on a direction.')),
        ('sec', 'switching', 'What about switching later?',
         P('Moving a website from one platform to another is often possible. What’s involved depends on where your site is now and where it’s going.') +
         P('It’s still worth choosing for where your business is heading, not just where it is today. A platform that fits your plans saves you from rebuilding sooner than you’d like.')),
    ],
    bottom='There’s no single best platform, only the best fit for your business. Squarespace keeps things simple and easy to manage, Shopify is built for selling and custom code gives you complete freedom. Tell me about your business and what you need your website to do, and I’ll recommend the platform that suits it.',
    practice=['callum', 'rooster', 'smash'],
),
dict(
    file='Guide-Branding.dc.html', key='Guide-Branding', tag='Brand and Marketing', short='What to have ready before branding or a website build',
    title_main='What to have ready before', title_em='branding or a website build',
    summary='Logo files, colours, fonts and photos: what helps, and what we can shape together.',
    meta_title='What to Have Ready Before Branding or a Website Build | Sullivan Park Design',
    meta_desc='Logo files, colours, fonts, photos and the words that describe you: a guide from Sullivan Park Design to preparing your brand before a design project.',
    hero=('/_blob/5cff939fb0c6c09242fc1bc76414a376', 'Five colour palettes from recent projects: SMASH, Hamish Ross, pARTy With Laura, The Rooster Den Co and Callum Frost'),
    intro='A consistent brand makes a business easier to recognise and easier to trust. Before we start on your website or marketing, it helps to know what you already have and what still needs defining. You don’t need a finished brand guide. Here’s what to gather, and what we can shape together.',
    takeaways=['Your logo, in the best file formats you have.', 'Your colours, with their exact codes if you know them.',
               'Your fonts, or a sense of the style you like.', 'Photos that show your work and your personality.',
               'A few words that describe how you want your business to feel.'],
    blocks=[
        ('sec', 'logo', 'Your logo files',
         P('Your logo is usually the starting point. Look for a vector version (SVG, EPS, AI or PDF), which can be resized without losing quality, and a PNG with a transparent background for everyday use.') +
         P('If you have more than one version, such as a stacked logo, a horizontal one or a small icon, gather them all. Each one is useful in different places, from the top of your website to a social profile picture.') +
         P(f'I don’t design logos, but if you have one you love, I can build the wider look around it. That’s what happened with {A("Party-With-Laura.dc.html", "pARTy With Laura")}, where the palette grew from her existing brush-script logo.')),
        ('sec', 'colours', 'Your colours',
         P('Note your brand colours and, if you know them, their codes. HEX codes (like #4E6368) are used on screens, while CMYK or Pantone values are used in print.') +
         P('A good palette usually has one or two main colours, an accent for buttons and highlights, and a few neutrals for backgrounds and text. If yours feels incomplete, or the colours don’t quite work together on screen, that’s something we can refine.') +
         P(f'Colour sets the mood, too. {A("Callum-Frost.dc.html", "Callum Frost")} wanted something classy and simple, so we chose black and white together and let his headshots do the talking.')),
        ('figure', '/_blob/c1b0714f4853e4cc5257cad7b3ca5bd0', 'A website colour palette board with five soft blue and green swatches above landscape photos'),
        ('sec', 'fonts', 'Your fonts',
         P('If your brand uses specific fonts, note their names and where they came from. Some fonts are free to use on websites, while others need a licence, so it’s worth checking before we start.') +
         P('If you don’t have brand fonts yet, think about the feel you’re after. An elegant serif can feel refined and established, while a clean sans serif can feel modern and approachable. Many brands pair one of each: one for headings and one for everyday text.')),
        ('sec', 'imagery', 'Your photos and imagery',
         P('Photos carry your brand as much as colours and fonts do. Gather your best photos of your work, your space and the people behind the business, in the largest size you have.') +
         P('Think about the style that feels like you, too: bright or moody, polished or relaxed, close-up details or wide open spaces. A consistent style across your website and marketing helps everything feel connected.')),
        ('quote', 'You don’t need a finished brand guide to start. You need a clear sense of how you want people to feel.'),
        ('sec', 'words', 'The words that describe you',
         P('Before any design decisions, it helps to put the feeling into words. Write down three to five words that describe how you want your business to feel. Calm, playful, luxurious, warm and bold all lead to very different designs.') +
         P('Then add a sentence about who you serve and what makes you different. It shapes the look as much as the copy, and it becomes the reference point for every choice that follows.')),
        ('sec', 'inspiration', 'Images you’re drawn to',
         P('Collect images that capture the feeling you want, from websites, magazines, interiors, nature or anywhere else. Don’t worry about why yet. Patterns tend to appear once you have a dozen or so.') +
         P('A mood board brings these together: a single page of colours, textures, type and photos that shows the direction before anything is designed. It’s a quick way to make sure we’re picturing the same thing.')),
        ('sec', 'where', 'Where your brand will appear',
         P('List the places your brand needs to work: your website, social media, newsletters, ads, signage, business cards or packaging. Knowing this early means colours, fonts and layouts are chosen to work everywhere, not just on screen.') +
         P(f'That’s how a look carries from a website into everyday marketing, like the monthly newsletters for {A("Smash.dc.html", "SMASH Performing Arts Studio")}, which share the same navy, gold and elegant serif headlines as the site.')),
    ],
    bottom='Whether you’re starting fresh or carrying an established look forward, gathering these pieces makes the design process faster and the result more consistent. If some are missing, that’s what we work out together. Tell me what you have, and we’ll take it from there.',
    practice=['rooster', 'smash', 'laura'],
),
dict(
    file='Guide-Search.dc.html', key='Guide-Search', tag='SEO', short='How to help Google and AI search find your business',
    title_main='How to help Google and AI search', title_em='find your business',
    summary='The foundations that help search engines and AI tools understand who you are and what you offer.',
    meta_title='How to Help Google and AI Search Find Your Business | Sullivan Park Design',
    meta_desc='A practical guide from Sullivan Park Design to the SEO and GEO foundations that help search engines and AI tools understand your business.',
    hero=('/_blob/99c229f238a46297d17abd3836a64f4e', 'Search result cards showing page titles and descriptions from pARTy With Laura and The Rooster Den Co'),
    intro='People now find businesses in two ways: through search results and through AI tools like ChatGPT, Perplexity and Google’s AI results. The good news is that both reward the same things: a clear, well-organized website that genuinely answers people’s questions. Here are the foundations I focus on, and the ones you can start on today.',
    takeaways=['Know the words and questions your customers actually use.', 'Give every page one clear purpose, title and description.',
               'Answer common questions in plain language.', 'Set up Google Business Profile and Search Console.',
               'Build steadily over time, never with shortcuts.'],
    blocks=[
        ('sec', 'customers', 'Start with how your customers search',
         P('Good SEO starts with knowing what your customers search for. Think about the words they use (which aren’t always the words you use), the questions they ask and the places they live or work.') +
         P('A real estate agent might think in terms of listings, while buyers search for homes for sale in White Rock. Writing for the way people actually search makes it much easier for them to find you.')),
        ('sec', 'pages', 'Give every page one clear job',
         P('Each important service or topic deserves its own page, with one clear heading that says exactly what it is. A single page trying to cover everything is harder for visitors and search engines to understand.') +
         P(f'Organize your menu around what people look for, too. On {A("Hamish-Ross.dc.html", "Hamish Ross Real Estate")}, the market report and journal sit in the main menu alongside listings, buying and selling.')),
        ('sec', 'titles', 'Write titles and descriptions that say what’s there',
         P('Every page has a title and a short description that can appear in search results. They’re often the first thing someone reads about your business, so make them specific: what the page offers, and where, if that matters.') +
         anatomy() +
         P('Vague titles like Services or Home waste that space. A title like Weekly Kids Art Classes in Cloverdale tells people, and search engines, exactly what they’ll find.')),
        ('quote', 'Clear, well-organized and genuinely useful content helps you in search results and in AI answers.'),
        ('sec', 'answers', 'Answer questions in plain language',
         P('AI tools in particular look for clear, direct answers. Pages that plainly explain what you offer, who it’s for, where you work and what happens next are easier for them to understand and mention.') +
         P('FAQs, service pages that explain the details and guides like this one all help. So does structured information behind the scenes (often called schema), which labels things like your business name, location and services so they can be read reliably.')),
        ('sec', 'local', 'Show where you are',
         P(f'If you serve a particular area, say so clearly in your page titles, headings and copy. Name the neighbourhoods and cities you serve, the way {A("Hamish-Ross.dc.html", "Hamish Ross Real Estate")} names White Rock, South Surrey and Ocean Park.') +
         P(f'Set up a Google Business Profile with accurate details, photos and hours, and keep your business name, address and phone number the same everywhere they appear online. I set one up for {A("Rooster-Den.dc.html", "The Rooster Den Co")} as part of the store’s redesign.')),
        ('sec', 'experience', 'Make your site easy to use',
         P('Search engines pay attention to the experience a site offers. Pages should load quickly, work well on phones and be easy to navigate. Descriptive image file names and alt text help too, for search and for people using screen readers.')),
        ('sec', 'tools', 'Connect the right tools',
         P('Google Search Console shows which searches bring people to your site and flags problems Google finds. Google Analytics shows what visitors do once they arrive. Both are free, and setting them up at launch means you have useful information from day one.')),
        ('sec', 'steady', 'Build steadily, without shortcuts',
         P('SEO builds over time. Some improvements can show up fairly quickly, while broader progress usually takes months of steady work. Be wary of anyone who promises fast rankings or a guaranteed spot.') +
         P('Avoid tricks like stuffing keywords into every sentence, creating near-identical pages for every town or buying links. They can do more harm than good. Useful content and a well-organized website are what last.')),
    ],
    bottom=f'You don’t need to master every detail of SEO to make progress. Start with clear pages, specific titles, plain-language answers and an accurate Google Business Profile, then keep improving over time. If you’d like help, I can look at where your website is now and make each page clearer, whether I built it or not.',
    practice=['hamish', 'rooster', 'smash'],
),
dict(
    file='Guide-Support.dc.html', key='Guide-Support', tag='Ongoing Support', short='What ongoing website and marketing support can include',
    title_main='What ongoing website and marketing support', title_em='can include',
    summary='SEO, content, newsletters and website updates: what it looks like to have someone keeping things moving.',
    meta_title='What Ongoing Website and Marketing Support Can Include | Sullivan Park Design',
    meta_desc='A guide from Sullivan Park Design to ongoing website and marketing support, from SEO and content to newsletters, social media and website updates.',
    hero=('/_blob/e3423a54ddc73a58c47dfc70bdc215f7', 'A laptop on a small table on a sunny balcony overlooking the sea, beside two cups of coffee and a vase of flowers'),
    intro='A website isn’t finished the day it launches. Your business changes, your customers’ questions change and search keeps moving. Ongoing support means someone is looking after your website and marketing so they keep up, without it landing on your to-do list. Here’s what it can include, and how to tell if it’s right for you.',
    takeaways=['A website works best when it’s kept current after launch.', 'Support can cover SEO, content, newsletters, social media and updates.',
               'Scope and priorities are agreed in advance, so you know what’s covered.', 'It suits you if you’d rather spend your time running your business.',
               'Even without support, a simple routine keeps your site healthy.'],
    blocks=[
        ('sec', 'why', 'Why a website needs looking after',
         P('Information goes out of date quickly: prices, programs, team members, photos and opening hours. An out-of-date page can quietly cost you trust, and search engines tend to favour sites that stay current and useful.') +
         P('Small, regular attention also keeps little problems from growing, like a broken link, a form that’s stopped sending or a page that no longer reflects how you work.')),
        ('sec', 'updates', 'Website updates',
         P(f'This is the everyday care: new photos, updated text, new pages, seasonal changes and fixes as they come up. For {A("Callum-Frost.dc.html", "Callum Frost")}, that means adding his new headshots and resume changes whenever he has them.')),
        ('sec', 'seo', 'SEO and website content',
         P(f'Ongoing SEO builds on the foundations set at launch. It can include planning content around what your customers search for, refining pages that could be clearer and keeping an eye on how your site appears in search. My {A("Guide-Search.dc.html", "guide to search and AI")} covers those foundations.') +
         P('Blogs and articles can be part of this, too, written around real customer questions rather than posted for the sake of it.')),
        ('sec', 'newsletters', 'Newsletters',
         P(f'A regular newsletter keeps you in touch with the people who already know you. As part of their ongoing support, I create the monthly newsletters for {A("Smash.dc.html", "SMASH Performing Arts Studio")}, sharing studio news and important dates with families.')),
        ('sec', 'social', 'Social content and marketing design',
         P('Social graphics, ads and printed pieces work best when they clearly belong to the same business as your website. Ongoing support can include designing these regularly, so your marketing stays consistent without you briefing someone new each time.')),
        ('quote', 'A website works hardest when someone is paying attention to it.'),
        ('sec', 'how', 'How ongoing support works',
         P('Every business needs something different. We agree on the scope and priorities in advance, so you know what I’m handling and how it supports your wider plans.') +
         P('It can focus on one area, like monthly newsletters, or bring several together around your business priorities, such as SEO, blogs, social content and website updates.')),
        ('sec', 'signs', 'Signs it might be time',
         ticks(['Your website has information you know is out of date.', 'Updates sit on your to-do list for weeks.',
                'Your marketing looks a little different every time.', 'You know SEO matters but don’t have time for it.',
                'You’d rather spend your time on your actual work.'])),
        ('sec', 'diy', 'If you’d rather do it yourself',
         P('Ongoing support isn’t for everyone, and plenty of small businesses look after their own sites. If that’s you, a simple routine goes a long way:') +
         ticks(['Check your key pages and contact form every month.', 'Update photos, prices and dates as soon as they change.',
                'Look at Search Console now and then for errors or new searches.', 'Keep your Google Business Profile hours and photos current.',
                'Review your main pages once a year to make sure they still reflect your business.'])),
    ],
    bottom='Ongoing support is about keeping your website and marketing moving, so they keep reflecting your business as it grows. If you’d like help with some or all of it, tell me what’s on your plate and we’ll work out the right scope together.',
    practice=['smash', 'callum', 'hamish'],
),
]
for i, g in enumerate(GUIDES):
    g['num'] = f'{i + 1:02d}'
    g['next'] = GUIDES[(i + 1) % len(GUIDES)]


# --------------------------------------------------------------- page plumbing
def swap_head(s, title, desc):
    s = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', s, count=1)
    for pat, val in [(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">'),
                     (r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title}">'),
                     (r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{desc}">')]:
        s = re.sub(pat, val, s, count=1)
    return s

def swap_main(s, main):
    a = s.index('<main id="main">'); b = s.index('</main>') + len('</main>')
    return s[:a] + '<main id="main">\n' + main + '\n</main>' + s[b:]

def swap_css(s, css, tag):
    start, end = f'/* {tag} */', f'/* /{tag} */'
    block = f'{start}\n{css}\n{end}\n'
    if start in s:
        a = s.index(start); b = s.index(end) + len(end) + 1
        return s[:a] + block + s[b:]
    return s.replace('/* NAV v2 (generated) */', block + '/* NAV v2 (generated) */', 1)

def set_preview(s, h):
    return re.sub(r'"\$preview":\{"width":1440,"height":\d+\}', f'"$preview":{{"width":1440,"height":{h}}}', s, count=1)

CLOSING_RE = re.compile(r'<!-- CLOSING -->.*?</section>', re.S)
GUIDE_CSS = '''.gd-cmp{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;margin:8px 0}
.gd-cmp-col{min-width:0;display:flex;flex-direction:column}
.gd-anat-row{display:grid;grid-template-columns:120px minmax(0,1fr);gap:8px 20px;align-items:baseline}
.gd-anat-lab{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#4E6368;padding-top:3px}
.gd-next{display:flex;align-items:center;justify-content:space-between;gap:24px;padding:24px 28px;border:1px solid rgba(78,99,104,.45);text-decoration:none;color:#121414;transition:background-color .4s,border-color .4s}
.gd-next:hover{background:#FAFAF8;border-color:#4E6368}
.gd-next-arrow{transition:transform .5s cubic-bezier(.2,.7,.2,1)}
.gd-next:hover .gd-next-arrow{transform:translateX(6px)}
@media (max-width: 760px){.gd-cmp{grid-template-columns:minmax(0,1fr);gap:36px}.gd-anat-row{grid-template-columns:minmax(0,1fr);gap:4px}}
@media (prefers-reduced-motion: reduce){.gd-next,.gd-next-arrow{transition:none}}'''


def build_guide(g, template, author, closing):
    sections = []
    body = [f'<p class="sp-dropcap" style="margin: 0; font-size: 21px; line-height: 1.8; color: {BODY}">{g["intro"]}</p>']
    for blk in g['blocks']:
        if blk[0] == 'sec':
            _, id_, title, html = blk
            sections.append((id_, title))
            body.append(f'''<section aria-labelledby="{id_}" style="display: flex; flex-direction: column; gap: 18px; padding-top: 28px">
<p aria-hidden="true" style="margin: 0; font-family: {SERIF}; font-style: italic; font-weight: 300; font-size: 56px; line-height: 1; color: {TEAL}">{len(sections):02d}</p>
<h2 id="{id_}" style="margin: 0; font-family: {SERIF}; font-weight: 400; font-size: clamp(32px, 3vw, 44px); line-height: 1.12; color: {INK}">{title}</h2>
{html}
</section>''')
        elif blk[0] == 'quote':
            body.append(quote(blk[1]))
        elif blk[0] == 'figure':
            body.append(figure(blk[1], blk[2]))
    body.append(f'''<section class="sp-on-dark sp-reveal" aria-labelledby="bottom-line" style="margin-top: 36px; background: {TEAL}; padding: 12px; box-shadow: 0 30px 70px rgba(18, 28, 30, 0.18)">
<div style="border: 1px solid rgba(255, 255, 255, 0.4); padding: clamp(30px, 4vw, 52px); display: flex; flex-direction: column; gap: 20px">
<h2 id="bottom-line" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(34px, 3.2vw, 48px); line-height: 1.1; color: #FFFFFF">The bottom <em style="font-style: italic; color: #DCE4E5">line</em></h2>
<p style="margin: 0; font-size: 19px; line-height: 1.8; color: #FFFFFF">{g['bottom']}</p>
<a class="sp-btn sp-btn-light" href="Contact.dc.html" style="align-self: flex-start; margin-top: 6px; display: inline-flex; align-items: center; justify-content: center; gap: 14px; min-height: 56px; padding: 0 30px; background: #FAFAF8; border: 1px solid #FAFAF8; color: {INK}; text-decoration: none; font-size: 18px; letter-spacing: 0.03em">Enquire About Your Project{ARROW}</a>
</div>
</section>''')
    words = len(re.sub(r'<[^>]+>', ' ', '\n'.join(body)).split()) + sum(len(t.split()) for t in g['takeaways'])
    g['read'] = max(1, round(words / 220))
    nx = g['next']
    body.append(author)
    body.append(f'''<a class="gd-next sp-reveal" href="{nx['file']}"><span style="display: flex; flex-direction: column; gap: 6px; min-width: 0"><span style="font-size: 13px; letter-spacing: 0.2em; text-transform: uppercase; color: {TEAL}">Next guide · {nx['num']}</span><span style="font-family: {SERIF}; font-size: clamp(24px, 2.2vw, 30px); line-height: 1.2; color: {INK}">{nx['short']}</span></span><span class="gd-next-arrow" aria-hidden="true" style="flex: none; color: {TEAL}"><svg width="30" height="12" viewBox="0 0 26 10" fill="none"><path d="M0 5h24M20 1l4 4-4 4" stroke="currentColor" stroke-width="1.1"></path></svg></span></a>''')
    body.append(f'<a class="sp-link" href="Journal.dc.html" style="align-self: flex-start; display: inline-flex; align-items: center; gap: 12px; min-height: 44px; color: {TEAL}; font-size: 17px; letter-spacing: 0.03em; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 6px">Browse All Guides{ARROW}</a>')

    li = 'border-bottom: 1px solid rgba(78, 99, 104, 0.3)'
    lk = 'display: flex; gap: 14px; padding: 12px 0; font-size: 16px; line-height: 1.45; color: #1F2426; text-decoration: none'
    nm = f'flex: none; width: 24px; font-family: {SERIF}; font-style: italic; font-size: 19px; color: {TEAL}'
    toc = ''.join(f'<li style="{li}"><a href="#{i}" style="{lk}"><span aria-hidden="true" style="{nm}">{n + 1:02d}</span>{t}</a></li>' for n, (i, t) in enumerate(sections))
    toc += f'<li style="{li}"><a href="#bottom-line" style="{lk}"><span aria-hidden="true" style="{nm}">·</span>The bottom line</a></li>'
    tk = ''.join(f'<li style="display: flex; gap: 14px; font-size: 17px; line-height: 1.6; color: #1F2426"><span aria-hidden="true" style="flex: none; width: 16px; height: 1px; margin-top: 13px; background: {TEAL}"></span><span>{t}</span></li>' for t in g['takeaways'])
    himg, halt = g['hero']

    article = f'''<article aria-labelledby="page-title">

<!-- GUIDE HERO -->
<header style="position: relative; overflow: hidden; background: #FAFAF8">
{PALM}
<div style="position: relative; z-index: 1; {WRAP}; padding: clamp(140px, 12vw, 176px) {GUTTER} clamp(56px, 6vw, 88px); display: flex; flex-direction: column; gap: clamp(48px, 5vw, 72px)">
<div style="display: flex; flex-direction: column; gap: 28px; max-width: 1260px">
{label(f'Guide {g["num"]} · {g["tag"]}')}
<h1 id="page-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(46px, 6.2vw, 102px); line-height: 1.02; letter-spacing: -0.015em; color: {INK}; text-wrap: balance">{g['title_main']} <em style="font-style: italic; color: {TEAL}">{g['title_em']}</em></h1>
<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 14px 22px; font-size: 16px; letter-spacing: 0.06em; color: {MUTED}">
<span style="display: inline-flex; align-items: center; gap: 14px"><img src="/_blob/61209a65a04271cd5c18338b2938e4f1" alt="" width="1000" height="1000" style="width: 48px; height: 48px; object-fit: cover; object-position: 50% 20%; border: 1px solid rgba(78, 99, 104, 0.35); padding: 3px; background: #FFFFFF"><span>By <span style="color: {INK}">Natasha</span></span></span>
<span aria-hidden="true" style="width: 24px; height: 1px; background: rgba(78, 99, 104, 0.5)"></span>
<span>{g['read']} min read</span>
</div>
</div>
<div style="position: relative; padding: 0 24px 24px 0">
<span aria-hidden="true" style="position: absolute; top: 24px; left: 24px; right: 0; bottom: 0; border: 1px solid rgba(78, 99, 104, 0.45)"></span>
<div class="sp-photo" style="position: relative"><img src="{himg}" alt="{halt}" width="1800" height="771" fetchpriority="high" style="width: 100%; aspect-ratio: 21 / 9; object-fit: cover"></div>
</div>
</div>
</header>

<!-- GUIDE BODY -->
<div style="background: #FFFFFF">
<div style="{WRAP}; padding: clamp(64px, 7vw, 104px) {GUTTER} clamp(80px, 9vw, 128px); display: flex; flex-wrap: wrap; justify-content: center; align-items: flex-start; gap: 48px clamp(40px, 5vw, 88px)">

<nav class="sp-toc" aria-label="In this guide" style="flex: 0 0 260px; min-width: 0; position: sticky; top: 104px; display: flex; flex-direction: column; gap: 18px">
<p style="margin: 0; display: flex; align-items: center; gap: 14px; font-size: 14px; letter-spacing: 0.2em; text-transform: uppercase; color: {TEAL}"><span aria-hidden="true" style="display: block; width: 28px; height: 1px; background: {TEAL}"></span>In This Guide</p>
<ol style="list-style: none; margin: 0; padding: 0; border-top: 1px solid rgba(78, 99, 104, 0.3)">{toc}</ol>
</nav>

<div style="flex: 1 1 600px; max-width: 760px; min-width: 0; display: flex; flex-direction: column; gap: 28px">

<aside class="sp-card" aria-labelledby="takeaways-title" style="background: #FAFAF8; padding: 12px; box-shadow: 0 24px 60px rgba(18, 28, 30, 0.08); margin-bottom: 16px">
<div style="border: 1px solid rgba(78, 99, 104, 0.3); padding: clamp(26px, 3vw, 40px); display: flex; flex-direction: column; gap: 16px">
<h2 id="takeaways-title" style="margin: 0; font-family: {SERIF}; font-weight: 400; font-size: 30px; line-height: 1.15; color: {INK}">Key <em style="font-style: italic; color: {TEAL}">takeaways</em></h2>
<ul style="list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 12px">{tk}</ul>
</div>
</aside>

{chr(10).join(body)}

</div>

<div class="sp-spacer" aria-hidden="true" style="flex: 0 0 260px"></div>

</div>
</div>

</article>'''

    cards = []
    for i, key in enumerate(g['practice']):
        href, img, tag, title, alt = CASES[key]
        off, mt = (' sp-offset', ' margin-top: clamp(0px, 4.5vw, 72px);') if i == 1 else ('', '')
        cards.append(f'''<a class="sp-reveal{off}" href="{href}" style="flex: 1 1 320px; min-width: 0;{mt} display: flex; flex-direction: column; gap: 20px; text-decoration: none; color: {INK}">
<div style="position: relative; padding: 0 16px 16px 0"><span aria-hidden="true" style="position: absolute; top: 16px; left: 16px; right: 0; bottom: 0; border: 1px solid rgba(78, 99, 104, 0.45)"></span><div class="sp-photo" style="position: relative; background: #FFFFFF"><img src="{img}" alt="{alt}" width="1800" height="1125" loading="lazy" style="width: 100%; aspect-ratio: 16 / 10; object-fit: cover; object-position: top"></div></div>
<p style="margin: 0; font-size: 15px; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}">{tag}</p>
<h3 class="sp-more-title" style="margin: 0; font-family: {SERIF}; font-weight: 400; font-size: 30px; line-height: 1.2; color: {INK}">{title}</h3>
</a>''')
    practice = f'''<!-- SEE IT IN PRACTICE -->
<section aria-labelledby="more-title" style="background: #ECEEED">
<div style="{WRAP}; padding: clamp(80px, 9vw, 128px) {GUTTER} clamp(104px, 11vw, 160px); display: flex; flex-direction: column; gap: clamp(40px, 5vw, 64px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 24px 64px">
<div style="display: flex; flex-direction: column; gap: 20px">
{label('See It in Practice')}
<h2 id="more-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(40px, 4.6vw, 70px); line-height: 1.04; color: {INK}">Projects <em style="font-style: italic; color: {TEAL}">from this guide</em></h2>
</div>
<a class="sp-btn sp-btn-line" href="Portfolio.dc.html" style="display: inline-flex; align-items: center; justify-content: center; min-height: 54px; padding: 0 28px; border: 1px solid {TEAL}; color: {TEAL}; text-decoration: none; font-size: 17px; letter-spacing: 0.03em">View All Work</a>
</div>
<div style="display: flex; flex-wrap: wrap; align-items: flex-start; gap: 48px clamp(24px, 2.6vw, 36px)">
{chr(10).join(cards)}
</div>
</div>
</section>'''

    s = swap_head(template, g['meta_title'], g['meta_desc'])
    s = swap_main(s, '\n\n'.join([article, practice, closing]))
    s = swap_css(s, GUIDE_CSS, 'GUIDES')
    s = set_preview(s, g.get('preview', 10000))
    return s


def build_resources(template):
    s = template
    closing = CLOSING_RE.search(s).group(0)
    g1 = GUIDES[0]
    a0 = s.index('<!-- HERO -->'); a1 = s.index('<!-- START HERE: Guide 01 -->')
    hero = s[a0:a1].rstrip()
    feature = f'''<!-- START HERE: Guide 01 -->
<section aria-labelledby="start-title" style="background: #FFFFFF">
<div style="{WRAP}; padding: clamp(72px, 8vw, 112px) {GUTTER}">
<a class="sp-feature sp-reveal" href="{g1['file']}" style="display: flex; flex-wrap: wrap; align-items: center; gap: 40px clamp(48px, 6vw, 104px); text-decoration: none; color: {INK}">
<div style="flex: 1.3 1 520px; min-width: 0; position: relative; padding: 0 24px 24px 0">
<span aria-hidden="true" style="position: absolute; top: 24px; left: 24px; right: 0; bottom: 0; border: 1px solid rgba(78, 99, 104, 0.45)"></span>
<div class="sp-photo" style="position: relative"><img src="/_blob/9095e97c95708cc67b261cafbb8c1d21" alt="An open, light-filled pavilion overlooking a calm sea" width="1200" height="800" loading="lazy" style="width: 100%; aspect-ratio: 3 / 2; object-fit: cover"></div>
</div>
<div style="flex: 1 1 380px; min-width: 0; display: flex; flex-direction: column; gap: 22px">
{label('Start Here · Guide 01')}
<h2 id="start-title" class="sp-feature-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(38px, 4vw, 62px); line-height: 1.06; color: {INK}; text-wrap: balance">{g1['short']}</h2>
<p style="margin: 0; font-size: 19px; line-height: 1.7; color: {BODY}">The goals, content, photos and logins worth gathering first, so your project starts smoothly and our time goes into the parts that matter most.</p>
<p style="margin: 0; font-size: 16px; letter-spacing: 0.08em; color: {MUTED}">{g1['read']} min read · Natasha</p>
<span style="align-self: flex-start; display: inline-flex; align-items: center; gap: 12px; min-height: 48px; color: {TEAL}; font-size: 18px; letter-spacing: 0.03em; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 7px">Read the Guide<svg width="26" height="10" viewBox="0 0 26 10" fill="none" aria-hidden="true"><path d="M0 5h24M20 1l4 4-4 4" stroke="currentColor" stroke-width="1.1"></path></svg></span>
</div>
</a>
</div>
</section>'''
    rows = []
    for g in GUIDES:
        rows.append(f'''<li class="sp-reveal"><a class="rs-row sp-row" href="{g['file']}"><span class="sp-visually-hidden">Guide {g['num']}: </span><span class="rs-num" aria-hidden="true">{g['num']}</span>
<span class="rs-main"><span class="rs-tag">{g['tag']} · {g['read']} min read</span><span class="rs-title sp-row-title">{g['short']}</span><span class="rs-desc">{g['summary']}</span></span>
<span class="rs-go sp-row-arrow" aria-hidden="true"><svg width="16" height="10" viewBox="0 0 26 10" fill="none"><path d="M0 5h24M20 1l4 4-4 4" stroke="currentColor" stroke-width="1.3"></path></svg></span></a></li>''')
    guides = f'''<!-- THE GUIDES -->
<section aria-labelledby="guides-title" style="background: #ECEEED">
<div style="{WRAP}; padding: clamp(80px, 9vw, 128px) {GUTTER}; display: flex; flex-direction: column; gap: clamp(36px, 4vw, 56px)">
<div class="sp-reveal" style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 20px clamp(48px, 7vw, 120px)">
<div style="flex: 1 1 480px; min-width: 0; display: flex; flex-direction: column; gap: 24px">
{label('The Guides')}
<h2 id="guides-title" style="margin: 0; font-family: {SERIF}; font-weight: 300; font-size: clamp(40px, 4.6vw, 70px); line-height: 1.04; color: {INK}; text-wrap: balance">Five guides, <em style="font-style: italic; color: {TEAL}">one for every step</em></h2>
</div>
<p style="flex: 1 1 420px; min-width: 0; margin: 0; font-size: 19px; line-height: 1.7; color: {BODY}">Each guide answers a question that comes up before a project begins, from planning and platforms to search and ongoing care.</p>
</div>
<ol class="rs-list">
{chr(10).join(rows)}
</ol>
</div>
</section>'''
    return swap_main(s, '\n\n'.join([hero, feature, guides, closing]))


def check_copy(name, s):
    main = s.split('<main id="main">')[1].split('</main>')[0]
    txt = re.sub(r'<[^>]+>', ' ', main)
    assert '—' not in txt and '--' not in txt, f'{name}: dash in copy'
    assert 'bespoke' not in txt.lower(), f'{name}: bespoke'


template = open(os.path.join(ROOT, 'Article.dc.html')).read()
a0 = template.index('<aside class="sp-card sp-reveal" aria-label="About the author"'); a1 = template.index('</aside>', a0) + len('</aside>')
AUTHOR = template[a0:a1]
CLOSING = CLOSING_RE.search(template).group(0)
PREVIEW = {'Article.dc.html': 10000, 'Guide-Platforms.dc.html': 9400, 'Guide-Branding.dc.html': 9800, 'Guide-Search.dc.html': 10000, 'Guide-Support.dc.html': 9600}
if os.path.exists(os.path.join(HERE, 'guide_heights.json')):
    PREVIEW.update(json.load(open(os.path.join(HERE, 'guide_heights.json'))))
outs = {}
for g in GUIDES:
    g['preview'] = PREVIEW[g['file']]
    outs[g['file']] = build_guide(g, template, AUTHOR, CLOSING)
outs['Journal.dc.html'] = build_resources(open(os.path.join(ROOT, 'Journal.dc.html')).read())
for name, s in outs.items():
    check_copy(name, s)
    open(os.path.join(ROOT, name), 'w').write(s)
    print('written', name, len(s))
print('read times', {g['file']: g['read'] for g in GUIDES})
