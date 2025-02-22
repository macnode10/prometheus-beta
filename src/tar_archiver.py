import os
import tarfile
from typing import Union, Optional

def create_tar_archive(
    source_dir: str, 
    output_path: Optional[str] = None, 
    compression: Optional[str] = 'gz'
) -> str:
    """
    Create a tar archive of a given directory.
    
    Args:
        source_dir (str): Path to the source directory to archive
        output_path (str, optional): Path where the tar archive will be saved. 
                                     If not provided, uses source directory name.
        compression (str, optional): Compression type. 
                                     Supports 'gz' (default), 'bz2', or None for no compression
    
    Returns:
        str: Path to the created tar archive
    
    Raises:
        ValueError: If source directory does not exist or is invalid
        PermissionError: If there are permission issues creating the archive
    """
    # Validate source directory
    source_dir = os.path.abspath(source_dir)
    
    if not os.path.exists(source_dir):
        raise ValueError(f"Source directory {source_dir} does not exist")
    
    if not os.path.isdir(source_dir):
        raise ValueError(f"Source path {source_dir} is not a directory")
    
    # Determine output path
    if output_path is None:
        output_path = os.path.basename(source_dir.rstrip('/')) + '.tar'
    else:
        output_path = os.path.abspath(output_path)
    
    # Add compression extension if needed
    if compression == 'gz':
        output_path += '.gz'
    elif compression == 'bz2':
        output_path += '.bz2'
    elif compression is not None:
        raise ValueError("Compression must be 'gz', 'bz2', or None")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Determine tarfile mode
    mode = 'w:' + (compression or '')
    
    try:
        with tarfile.open(output_path, mode) as tar:
            # Add directory contents, preserving relative structure
            tar.add(source_dir, arcname=os.path.basename(source_dir))
    except PermissionError:
        raise PermissionError(f"Permission denied when creating archive at {output_path}")
    
    return output_path