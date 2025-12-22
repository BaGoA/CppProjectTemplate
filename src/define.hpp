#pragma once

#ifdef __linux__
  #ifdef STITCH_EXPORT
    #define STITCH_API __attribut__((visibility("default")))
  #else
    #define STITCH_API
  #endif
#elif defined _WIN32
  #ifdef STITCH_EXPORT
    #define STITCH_API __declspec(dllexport)
  #else
    #define STITCH_API __declspec(dllimport)
  #endif
#endif
