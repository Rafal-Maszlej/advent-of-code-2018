import pytest

from solver import ImageDecoder


@pytest.fixture
def image_data_fake():
    return {
        "width": 3,
        "height": 2,
        "data": "123210709012"
    }


@pytest.fixture
def image_data_real():
    return {
        "width": 2,
        "height": 3,
        "data": "022201112220221211000000"
    }


def test_split_layers(image_data_fake):
    decoder = ImageDecoder(**image_data_fake)
    expected_layers = ["123210", "709012"]
    layers = decoder.split_layers()

    assert layers == expected_layers


def test_get_signature(image_data_fake):
    decoder = ImageDecoder(**image_data_fake)
    expected_signature = 4
    signature = decoder.get_signature()

    assert signature == expected_signature


def test_get_pixels(image_data_real):
    decoder = ImageDecoder(**image_data_real)
    expected_pixels = ["0120", "2120", "2210", "2220", "0210", "1010"]
    pixels = decoder.get_pixels()

    assert pixels == expected_pixels


def test_decode_pixels(image_data_real):
    decoder = ImageDecoder(**image_data_real)
    expected_image = [(0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255)]
    image = decoder.decode_pixels()

    assert image == expected_image


if __name__ == "__main__":
    pytest.main([__file__])
