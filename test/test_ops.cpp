#include "catch2/catch_all.hpp"

#include "ops.hpp"

TEST_CASE("Test add operation", "[ops]")
{
  const double x{1.0};
  const double y{1.0};
  const double sum{add(x, y)};
  REQUIRE(sum == Catch::Approx(x + y));
}
