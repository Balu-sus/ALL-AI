import torch
from diffusers import StableDiffusionPipeline

def generate_image_local(prompt: str, output_path: str = "generated_image.png"):
    """Generates an image locally using Stable Diffusion v1.5."""
    model_id = "runwayml/stable-diffusion-v1-5"
    
    # Use GPU if available (CUDA), otherwise fall back to CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if device == "cuda" else torch.float32

    print(f"Loading model on {device.upper()}...")
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id, 
        torch_dtype=torch_dtype
    )
    pipe = pipe.to(device)

    print(f"Generating image for prompt: '{prompt}'")
    image = pipe(prompt).images[0]
    
    image.save(output_path)
    print(f"Image saved successfully to {output_path}")

if __name__ == "__main__":
    generate_image_local("A futuristic server room with holographic displays, photorealistic")
