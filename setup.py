import cx_Freeze
from cx_Freeze import setup, Executable

# Define the executable and include relevant files
executables = [Executable("bmi_calculator.py", target_name="BMICalculatorApp.exe", base="Win32GUI")]

# Define setup options
setup(
    name="BMI Calculator",
    version="1.0",
    description="BMI Calculator Application",
    author="Aditya Janjanam",  # Add author name here
    author_email="janjanamaditya@gmail.com",  # Add author email (optional)
    executables=executables,
    options={
        'build_exe': {
            'packages': ["ttkbootstrap", "tkinter"],
            'include_files': []  # Add any additional files like images here
        },
        'bdist_msi': {
            'upgrade_code': "{YOUR-UNIQUE-UPGRADE-CODE}",
            'add_to_path': False,
            'initial_target_dir': r"[ProgramFilesFolder]\BMI Calculator",
            'summary_data': {
                "author": "Aditya Janjanam",  # Add author information in the MSI metadata
                "comments": "This application calculates BMI with a modern UI.",  # Optional description
            },
        },
    }
)
