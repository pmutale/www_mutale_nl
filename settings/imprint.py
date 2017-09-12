import git

repo = git.Repo()
if hasattr(repo, 'head') and repo.head.is_detached:
    branch = repo.head.object.hexsha
else:
    branch = format(repo.active_branch)

SITE_IMPRINT_DEV = 'development:' + branch
SITE_IMPRINT_ACC = 'acceptance' + branch
SITE_IMPRINT_PRD = 'production'

