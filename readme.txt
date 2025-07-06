## Usage Instructions

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run tests:**
```bash
# Run all tests
python run_tests.py

# Run specific suite
python run_tests.py --suite login_tests

# Run with specific browser and environment
python run_tests.py --env staging --browser firefox --headless

# Run with tags
python run_tests.py --tags "smoke AND NOT slow"
```

3. **Generate reports:**
```bash
# Reports are automatically generated in reports/ directory
# View report.html for detailed test results
```

## Key Features

- **Modular architecture** with separate concerns
- **Page Object Model** implementation
- **Environment-specific configuration**
- **Robust waiting mechanisms**
- **Screenshot capture on failures**
- **Parallel test execution support**
- **Data-driven testing capabilities**
- **Comprehensive logging and reporting**
- **Cross-browser support**
- **CI/CD integration ready**

This framework provides a solid foundation for web UI automation using Robot Framework with Python, following best practices and industry standards.
