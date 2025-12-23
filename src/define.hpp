#pragma once

#ifdef __linux__
  #ifdef CPP_PROJECT_EXPORT
    #define CPP_PROJECT_API __attribut__((visibility("default")))
  #else
    #define CPP_PROJECT_API
  #endif
#elif defined _WIN32
  #ifdef CPP_PROJECT_EXPORT
    #define CPP_PROJECT_API __declspec(dllexport)
  #else
    #define CPP_PROJECT_API __declspec(dllimport)
  #endif
#endif
