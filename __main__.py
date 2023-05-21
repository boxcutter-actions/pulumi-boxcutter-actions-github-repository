"""Manage boxcutter-actions org """

from boxcutter.scm.github import GitHubRepository, GitHubRepositoryArgs

GitHubRepository(
    "test-kitchen",
    GitHubRepositoryArgs(description="Test Kitchen GitHub Action"),
)
