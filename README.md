# ComfyUI Tag Limiter

A custom ComfyUI node that limits the number of tags in a comma-separated string. This is particularly useful for text-to-image workflows where you want to control the maximum number of prompt tags to avoid overwhelming the model or to maintain focus on key concepts.

## Features

- **Tag Count Limiting**: Restricts the number of tags to a specified maximum
- **Quote Preservation**: Maintains surrounding quotes if present in the input
- **Smart Parsing**: Handles comma-separated tags with proper whitespace trimming
- **Empty Tag Filtering**: Automatically removes empty tags from trailing commas
- **ComfyUI Integration**: Seamless integration with the ComfyUI workflow system

## Installation

### Method 1: Manual Installation

1. Download or clone this repository
2. Copy the `tag_limiter.py` file to your ComfyUI custom nodes directory:
   ```
   ComfyUI/custom_nodes/
   ```
3. Restart ComfyUI

### Method 2: Using Git

```bash
cd ComfyUI/custom_nodes/
git clone [repository-url] tag-limiter
```

## Usage

### Node Configuration

The Tag Limiter node has two input parameters:

- **text** (STRING): The comma-separated text containing tags to be limited
- **limit** (INT): The maximum number of tags to keep (default: 10)

### Example Workflows

#### Basic Tag Limiting

```
Input: "cat, dog, bird, fish, rabbit, hamster, turtle, snake, lizard, frog, mouse"
Limit: 5
Output: "cat, dog, bird, fish, rabbit"
```

#### With Quotes

```
Input: "cat, dog, bird, fish"
Limit: 2
Output: "cat, dog"
```

#### Handling Empty Tags

```
Input: "cat, dog, , bird, , fish,"
Limit: 3
Output: "cat, dog, bird"
```

### Integration in Workflows

The Tag Limiter node is particularly useful in these scenarios:

1. **Prompt Optimization**: Limit complex prompts to focus on essential concepts
2. **Batch Processing**: Ensure consistent tag counts across multiple images
3. **Model Performance**: Prevent tag overload that might affect generation quality
4. **Creative Constraints**: Artistic limitation for more focused results

## Node Category

The Tag Limiter node appears in the ComfyUI node browser under the category: `tag_limiter`

## Technical Details

### Input Processing

1. **Quote Detection**: The node checks if the input text is surrounded by quotes
2. **Content Extraction**: If quotes are present, they are temporarily removed for processing
3. **Tag Parsing**: Text is split by commas and each tag is stripped of whitespace
4. **Empty Tag Filtering**: Empty tags (from trailing commas) are automatically removed
5. **Limiting**: Only the first N tags are kept based on the specified limit
6. **Quote Restoration**: If quotes were originally present, they are re-added to the result

### Return Values

- **Output**: A STRING containing the limited tags, formatted as comma-separated values
- **Quote Preservation**: Original quote formatting is maintained in the output

## Examples

### Example 1: Basic Usage

```python
# Input text with many tags
text = "sunset, mountains, lake, trees, clouds, birds, flowers, grass, rocks, water"
limit = 5

# Result: "sunset, mountains, lake, trees, clouds"
```

### Example 2: With Surrounding Quotes

```python
# Input with quotes
text = '"red, blue, green, yellow, purple, orange"'
limit = 3

# Result: "red, blue, green"
```

### Example 3: Handling Edge Cases

```python
# Input with empty tags and trailing commas
text = "apple, banana, , cherry, , date,"
limit = 4

# Result: "apple, banana, cherry, date"
```

## Troubleshooting

### Common Issues

1. **No Output**: Ensure the input text contains comma-separated values
2. **Unexpected Results**: Check for proper comma separation and whitespace
3. **Quote Issues**: The node preserves quotes automatically - no manual handling needed

### Performance Notes

- The node processes text efficiently with minimal overhead
- Large tag lists are handled gracefully with the limit parameter
- No special memory requirements or performance constraints

## Compatibility

- **ComfyUI Version**: Compatible with ComfyUI 0.1.0 and later
- **Python Version**: Requires Python 3.7+
- **Dependencies**: No external dependencies required

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue on the GitHub repository
- Check the ComfyUI documentation for general node usage
- Review the examples in this README for common use cases