import git

# Clone a repository
#git.Repo.clone_from('https://github.com/username/repository.git', '/path/to/local')

# Pull changes from an existing repository
repo = git.Repo('https://github.com/samuels97/flasky.git')
origin = repo.remote(name='origin')
origin.pull()
