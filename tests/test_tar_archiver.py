import os
import pytest
import tarfile
import tempfile
import shutil

from src.tar_archiver import create_tar_archive

def test_create_tar_archive_default():
    """Test creating a tar archive with default settings"""
    with tempfile.TemporaryDirectory() as source_dir:
        # Create some test files
        with open(os.path.join(source_dir, 'test1.txt'), 'w') as f:
            f.write('test content')
        with open(os.path.join(source_dir, 'test2.txt'), 'w') as f:
            f.write('another test content')
        
        # Create archive
        archive_path = create_tar_archive(source_dir)
        
        # Verify archive exists and is a valid tar.gz
        assert os.path.exists(archive_path)
        assert archive_path.endswith('.tar.gz')
        
        # Verify contents of archive
        with tarfile.open(archive_path, 'r:gz') as tar:
            members = tar.getmembers()
            assert len(members) > 0
            # Verify directory structure
            dir_name = os.path.basename(source_dir)
            assert any(member.name.startswith(dir_name) for member in members)

def test_create_tar_archive_no_compression():
    """Test creating a tar archive without compression"""
    with tempfile.TemporaryDirectory() as source_dir:
        with open(os.path.join(source_dir, 'test.txt'), 'w') as f:
            f.write('test')
        
        archive_path = create_tar_archive(source_dir, compression=None)
        
        assert os.path.exists(archive_path)
        assert archive_path.endswith('.tar')
        
        with tarfile.open(archive_path, 'r:') as tar:
            members = tar.getmembers()
            assert len(members) > 0

def test_create_tar_archive_bz2_compression():
    """Test creating a tar archive with bz2 compression"""
    with tempfile.TemporaryDirectory() as source_dir:
        with open(os.path.join(source_dir, 'test.txt'), 'w') as f:
            f.write('test')
        
        archive_path = create_tar_archive(source_dir, compression='bz2')
        
        assert os.path.exists(archive_path)
        assert archive_path.endswith('.tar.bz2')
        
        with tarfile.open(archive_path, 'r:bz2') as tar:
            members = tar.getmembers()
            assert len(members) > 0

def test_create_tar_archive_custom_output():
    """Test creating archive with a custom output path"""
    with tempfile.TemporaryDirectory() as source_dir:
        # Create a test file
        with open(os.path.join(source_dir, 'test.txt'), 'w') as f:
            f.write('test')
        
        # Use a custom output path in a different directory
        with tempfile.TemporaryDirectory() as output_dir:
            custom_output = os.path.join(output_dir, 'custom_archive.tar.gz')
            archive_path = create_tar_archive(source_dir, output_path=custom_output)
            
            assert archive_path == custom_output
            assert os.path.exists(archive_path)

def test_create_tar_archive_invalid_source():
    """Test handling of non-existent source directory"""
    with pytest.raises(ValueError, match="does not exist"):
        create_tar_archive('/path/to/nonexistent/directory')

def test_create_tar_archive_not_directory():
    """Test handling when source is not a directory"""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(ValueError, match="is not a directory"):
            create_tar_archive(temp_file.name)