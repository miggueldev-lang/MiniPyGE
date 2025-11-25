from git_filter_repo import Commit

def commit_callback(commit: Commit):
    bad_emails = [
        b"169060996+MateusJuan@users.noreply.github.com"
    ]

    if commit.author_email in bad_emails:
        commit.author_name = b"miggueldev-lang"
        commit.author_email = b"migguel.dev@gmail.com"

    if commit.committer_email in bad_emails:
        commit.committer_name = b"miggueldev-lang"
        commit.committer_email = b"migguel.dev@gmail.com"
