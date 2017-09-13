import git
repository = git.Repo()
current_branch = format(repository.active_branch)
