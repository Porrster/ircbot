"""Everything is broken."""


def register(bot):
    bot.listen(r"^why (doesn't anything work|isn't anything working)$",
               theory_practice, require_mention=True)


def theory_practice(bot, msg):
    # Slightly modified from a sign written by daradib or sanjayk or whoever
    # As of this writing, it's still posted in the OCF lab
    # Original can be found at https://www.ocf.berkeley.edu/~daradib/dl/ocf/publicity/signs/theory-practice.odt
    msg.respond('\x1fTheory\x1f is when you know everything but nothing works.',
                ping=False)
    msg.respond('\x1fPractice\x1f is when everything works but nobody knows why.',
                ping=False)
    msg.respond('At the OCF, \x1ftheory and practice\x1f are \x02combined\x02: '
                'nothing works and nobody knows why.',
                ping=False)
