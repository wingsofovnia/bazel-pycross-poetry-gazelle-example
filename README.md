# bazel-pycross-poetry-gazelle-example

### Useful Commands
```
> poetry add ...                 # Add new dependency
> poetry lock                    # Update poetry.lock
> bazel run //:gazelle.update    # Update gazelle_python.yaml used by Gazelle
> bazel run //:gazelle.check     # Show changes needed to build scripts per Gazelle
> bazel run //:gazelle.update    # Apply changes needed to build scripts per Gazelle
> bazel run //:app               # Run Flask hello world app
> bazel run //:buildifier.fix    # Format *.bazel files
```