#pragma once

#include "spdlog/spdlog.h"
#include "spdlog/sinks/stdout_color_sinks.h"
#include "fmt/ostream.h"

namespace is {

using loglevel = spdlog::level::level_enum;

std::shared_ptr<spdlog::logger> logger();

void set_loglevel(std::shared_ptr<spdlog::logger> const& logger, loglevel);
void set_loglevel(loglevel);

template <class... Args>
inline void info(Args&&... args) {
  logger()->info(args...);
}

template <class... Args>
inline void warn(Args&&... args) {
  logger()->warn(args...);
}

template <class... Args>
inline void error(Args&&... args) {
  logger()->error(args...);
}

template <class... Args>
inline void critical(Args&&... args) {
  logger()->critical(args...);
  std::exit(-1);
}

}  // namespace is