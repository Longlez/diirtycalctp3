import pytest
import math
from DirtyCalc import calculate_delta, solve_quadratic


class TestCalculateDelta:
    """Tests pour la fonction calculate_delta."""
    
    def test_delta_positive(self):
        """Test delta > 0 (deux solutions réelles)."""
        delta = calculate_delta(1, -5, 6)
        assert delta == 1
    
    def test_delta_zero(self):
        """Test delta == 0 (une seule solution)."""
        delta = calculate_delta(1, -2, 1)
        assert delta == 0
    
    def test_delta_negative(self):
        """Test delta < 0 (solutions imaginaires)."""
        delta = calculate_delta(1, 0, 1)
        assert delta == -4
    
    def test_delta_large_values(self):
        """Test avec des valeurs plus grandes."""
        delta = calculate_delta(2, 10, 8)
        assert delta == 100 - 64
        assert delta == 36
    
    def test_delta_negative_coefficients(self):
        """Test avec des coefficients négatifs."""
        delta = calculate_delta(-1, 5, -6)
        assert delta == 25 - 24
        assert delta == 1


class TestSolveQuadratic:
    """Tests pour la fonction solve_quadratic."""
    
    # Tests pour delta > 0 (deux solutions réelles)
    def test_two_real_solutions(self):
        """Test équation x² - 5x + 6 = 0 (solutions: 2, 3)."""
        result = solve_quadratic(1, -5, 6)
        assert result["type"] == "deux_solutions"
        assert result["delta"] == 1
        assert result["x1"] == 2.0
        assert result["x2"] == 3.0
    
    def test_two_solutions_different_coefficients(self):
        """Test équation 2x² + 3x - 2 = 0."""
        result = solve_quadratic(2, 3, -2)
        assert result["type"] == "deux_solutions"
        assert result["delta"] == 25
        # x1 = (-3 - 5) / 4 = -2
        # x2 = (-3 + 5) / 4 = 0.5
        assert result["x1"] == -2.0
        assert result["x2"] == 0.5
    
    # Tests pour delta == 0 (une seule solution)
    def test_unique_solution(self):
        """Test équation x² - 2x + 1 = 0 (solution: 1)."""
        result = solve_quadratic(1, -2, 1)
        assert result["type"] == "unique"
        assert result["delta"] == 0
        assert result["solution"] == 1.0
    
    def test_unique_solution_other_values(self):
        """Test équation 4x² + 4x + 1 = 0 (solution: -0.5)."""
        result = solve_quadratic(4, 4, 1)
        assert result["type"] == "unique"
        assert result["delta"] == 0
        assert result["solution"] == -0.5
    
    # Tests pour delta < 0 (solutions imaginaires)
    def test_imaginary_solutions(self):
        """Test équation x² + 1 = 0 (solutions: ±i)."""
        result = solve_quadratic(1, 0, 1)
        assert result["type"] == "imaginaire"
        assert result["delta"] == -4
        assert result["real_part"] == 0.0
        assert result["imaginary_part"] == 1.0
    
    def test_imaginary_solutions_complex(self):
        """Test équation x² - 2x + 2 = 0."""
        result = solve_quadratic(1, -2, 2)
        assert result["type"] == "imaginaire"
        assert result["delta"] == -4
        # real_part = -(-2) / 2 = 1
        # imaginary_part = sqrt(4) / 2 = 1
        assert result["real_part"] == 1.0
        assert result["imaginary_part"] == 1.0
    
    # Tests avec différents coefficients a
    def test_negative_coefficient_a(self):
        """Test avec a négatif: -x² + 5x - 6 = 0."""
        result = solve_quadratic(-1, 5, -6)
        assert result["type"] == "deux_solutions"
        # x1 = (-5 - 1) / -2 = 3
        # x2 = (-5 + 1) / -2 = 2
        assert result["x1"] == 3.0
        assert result["x2"] == 2.0
    
    def test_fractional_results(self):
        """Test avec résultats fractionnaires: 3x² - x - 1 = 0."""
        result = solve_quadratic(3, -1, -1)
        assert result["type"] == "deux_solutions"
        # x1 = (1 - sqrt(13)) / 6
        # x2 = (1 + sqrt(13)) / 6
        expected_x1 = (1 - math.sqrt(13)) / 6
        expected_x2 = (1 + math.sqrt(13)) / 6
        assert abs(result["x1"] - expected_x1) < 1e-10
        assert abs(result["x2"] - expected_x2) < 1e-10
    
    # Tests avec coefficients décimaux
    def test_decimal_coefficients(self):
        """Test avec des coefficients décimaux: 0.5x² - 1.5x + 1 = 0."""
        result = solve_quadratic(0.5, -1.5, 1)
        assert result["type"] == "deux_solutions"
        assert result["delta"] == 2.25 - 2.0
        # x1 = (1.5 - 0.5) / 1 = 1
        # x2 = (1.5 + 0.5) / 1 = 2
        assert abs(result["x1"] - 1.0) < 1e-10
        assert abs(result["x2"] - 2.0) < 1e-10


class TestEdgeCases:
    """Tests pour les cas limites."""
    
    def test_zero_delta_very_small_coefficient_a(self):
        """Test avec a très petit mais non zéro."""
        result = solve_quadratic(0.0001, -0.0002, 0.0001)
        assert result["type"] == "unique"
        assert abs(result["delta"]) < 1e-9
    
    def test_large_values(self):
        """Test avec de grandes valeurs."""
        result = solve_quadratic(1000, -5000, 6000)
        assert result["type"] == "deux_solutions"
        # Les solutions doivent être valides
        assert isinstance(result["x1"], float)
        assert isinstance(result["x2"], float)
    
    def test_mixed_positive_negative(self):
        """Test avec coefficients positifs et négatifs mélangés."""
        result = solve_quadratic(1, 5, 6)
        assert result["type"] == "deux_solutions"
        # (x + 2)(x + 3) = x² + 5x + 6
        assert result["x1"] == -3.0
        assert result["x2"] == -2.0


class TestResultStructure:
    """Tests pour la structure des résultats retournés."""
    
    def test_result_has_delta_key(self):
        """Chaque résultat doit contenir la clé 'delta'."""
        result = solve_quadratic(1, -5, 6)
        assert "delta" in result
        assert isinstance(result["delta"], (int, float))
    
    def test_result_has_type_key(self):
        """Chaque résultat doit contenir la clé 'type'."""
        result = solve_quadratic(1, -5, 6)
        assert "type" in result
        assert result["type"] in ["unique", "deux_solutions", "imaginaire"]
    
    def test_unique_solution_result_structure(self):
        """Résultat unique doit avoir 'solution'."""
        result = solve_quadratic(1, -2, 1)
        assert "solution" in result
        assert "x1" not in result
        assert "x2" not in result
    
    def test_two_solutions_result_structure(self):
        """Résultat deux solutions doit avoir 'x1' et 'x2'."""
        result = solve_quadratic(1, -5, 6)
        assert "x1" in result
        assert "x2" in result
        assert "solution" not in result
    
    def test_imaginary_result_structure(self):
        """Résultat imaginaire doit avoir 'real_part' et 'imaginary_part'."""
        result = solve_quadratic(1, 0, 1)
        assert "real_part" in result
        assert "imaginary_part" in result
        assert "x1" not in result
        assert "x2" not in result
