# ./simulated-twin/app.py

from app import main
from dotenv import load_dotenv

# Check if the script is being executed as the main module
if __name__ == '__main__':
    # Load environment variables from the .env file into the environment
    load_dotenv()
    
    # Call the main function from the app module
    main()

