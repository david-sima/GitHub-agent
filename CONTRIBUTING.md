# Contributing to GitHub Agent

Thank you for your interest in contributing to the GitHub Agent project! This document provides guidelines and information for contributors.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- A GitHub account

### Development Setup

1. **Fork the repository**
   ```bash
   # Clone your fork
   git clone https://github.com/YOUR_USERNAME/github-agent.git
   cd github-agent
   ```

2. **Set up the development environment**
   ```bash
   # Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install development dependencies
   pip install -r requirements-dev.txt
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Guidelines

### Code Style

We use the following tools to maintain code quality:

- **Black**: Code formatting
- **Flake8**: Linting
- **MyPy**: Type checking
- **Pytest**: Testing

Run these tools before submitting your changes:

```bash
# Format code
black src/ tests/

# Check linting
flake8 src/ tests/

# Type checking
mypy src/

# Run tests
pytest
```

### Testing

- Write tests for all new functionality
- Ensure all existing tests pass
- Aim for good test coverage
- Use descriptive test names

Example test structure:

```python
def test_mcp_server_initialization():
    """Test that MCP server initializes correctly."""
    server = MCPServer()
    assert server.host == "localhost"
    assert server.port == 8000
    assert not server.running
```

### Documentation

- Update documentation for any new features
- Include docstrings for all public functions and classes
- Update the README if necessary
- Add examples for new functionality

### Commit Messages

Use clear, descriptive commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

Example:
```
Add MCP server authentication support

- Implement token-based authentication
- Add security configuration options
- Include unit tests for auth functionality

Fixes #123
```

## Pull Request Process

1. **Create a pull request** from your feature branch to the main branch
2. **Provide a clear description** of the changes
3. **Reference any related issues** in the description
4. **Ensure all tests pass** and code quality checks are satisfied
5. **Request review** from maintainers

### Pull Request Template

```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented if necessary)
```

## Issue Reporting

When reporting issues, please include:

- **Clear description** of the problem
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Environment details** (OS, Python version, etc.)
- **Error messages** or logs if applicable

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please:

- Be respectful and considerate of others
- Use inclusive language
- Be open to constructive feedback
- Help others learn and grow

## Getting Help

If you need help with contributing:

- Check existing issues and pull requests
- Join our community discussions
- Ask questions in the issues section
- Review the documentation

## Recognition

Contributors will be recognized in:

- The project README
- Release notes
- Contributor statistics

Thank you for contributing to the GitHub Agent project! 🚀 
