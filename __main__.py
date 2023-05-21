"""Manage boxcutter-actions org"""

import pulumi_github
from boxcutter.scm.github import GitHubRepository, GitHubRepositoryArgs

GitHubRepository(
    "test-kitchen",
    GitHubRepositoryArgs(
        description="Test Kitchen GitHub Action"
    ),
)
