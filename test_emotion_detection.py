"""Unit tests for the emotion detection application."""

import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_joy(self):
        """Test joy detection."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Test anger detection."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """Test disgust detection."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_fear(self):
        """Test fear detection."""
        result = emotion_detector("I am so afraid of this")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_sadness(self):
        """Test sadness detection."""
        result = emotion_detector("I am very sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")


if __name__ == "__main__":
    unittest.main()