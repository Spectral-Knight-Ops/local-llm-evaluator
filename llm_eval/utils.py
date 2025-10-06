import os
import ollama


def get_available_models():
    """Fetch and return list of available ollama models"""
    try:
        models = ollama.list()
        # Handle different response formats from ollama
        if hasattr(models, "models"):
            return [model.model for model in models.models]
        elif isinstance(models, dict) and "models" in models:
            return [model["name"] for model in models["models"]]
        elif isinstance(models, list):
            return [model.get("name", str(model)) for model in models]
        else:
            print(f"Unexpected response format: {type(models)}")
            print(f"Response content: {models}")
            return []
    except Exception as e:
        print(f"Error fetching models: {e}")
        return []


def select_models_interactively():
    """Allow user to select models interactively"""
    available_models = get_available_models()

    if not available_models:
        print("No models found. Please install models using 'ollama pull <model_name>'")
        return []

    print("\nAvailable models:")
    for i, model in enumerate(available_models, 1):
        print(f"{i}. {model}")

    while True:
        try:
            selection = input(
                "\nEnter model numbers separated by commas (e.g., 1,3,5): "
            ).strip()
            if not selection:
                print("No selection made. Exiting.")
                return []

            selected_indices = [int(x.strip()) - 1 for x in selection.split(",")]
            selected_models = []

            for idx in selected_indices:
                if 0 <= idx < len(available_models):
                    selected_models.append(available_models[idx])
                else:
                    print(f"Invalid selection: {idx + 1}. Please try again.")
                    break
            else:
                return selected_models

        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")


def clear_console():
    """Clear the console screen"""
    os.system('clear' if os.name == 'posix' else 'cls')