class TagLimiter:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
                "limit": ("INT", {"default": 40, "min": 0, "max": 1000, "step": 1}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "limit_tags"
    CATEGORY = "tag_limiter"

    def limit_tags(self, text, limit):
        # Check for surrounding quotes
        has_quotes = text.startswith('"') and text.endswith('"')
        
        if has_quotes:
            # Strip quotes for processing
            content = text[1:-1]
        else:
            content = text
            
        # Split by comma and strip whitespace from each tag
        # Filtering out empty tags in case of trailing commas
        tags = [t.strip() for t in content.split(',') if t.strip()]
        
        # Keep only the first N tags
        limited_tags = tags[:limit]
        
        # Join back with comma and space
        result = ", ".join(limited_tags)
        
        # Re-add quotes if they were originally present
        if has_quotes:
            result = f'"{result}"'
            
        return (result,)

NODE_CLASS_MAPPINGS = {
    "TagLimiter": TagLimiter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TagLimiter": "Tag Limiter"
}
