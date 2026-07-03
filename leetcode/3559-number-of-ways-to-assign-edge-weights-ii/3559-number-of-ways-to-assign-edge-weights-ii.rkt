(define/contract (assign-edge-weights edges queries)
  (-> (listof (listof exact-integer?))
      (listof (listof exact-integer?))
      (listof exact-integer?))

  (define MOD 1000000007)
  (define LOG 18)

  ;; Used n to store number of nodes.
  (define n (+ (length edges) 1))

  ;; Built adjacency list for the tree.
  (define graph
    (make-vector (+ n 1) '()))

  (for ([e edges])
    (define u (first e))
    (define v (second e))

    (vector-set!
     graph
     u
     (cons v (vector-ref graph u)))

    (vector-set!
     graph
     v
     (cons u (vector-ref graph v))))

  ;; Used depth to store node depths.
  (define depth
    (make-vector (+ n 1) 0))

  ;; Used up for binary lifting ancestors.
  (define up
    (build-vector
     LOG
     (λ (_) (make-vector (+ n 1) 0))))

  ;; Built depths and immediate parents using BFS.
  (define visited
    (make-vector (+ n 1) #f))

  (define queue (make-vector (+ n 5) 0))

  (define head 0)
  (define tail 1)

  (vector-set! queue 0 1)
  (vector-set! visited 1 #t)

  (let bfs ()
    (when (< head tail)

      (define node
        (vector-ref queue head))

      (set! head (+ head 1))

      (for ([next (vector-ref graph node)])

        (unless (vector-ref visited next)

          (vector-set!
           visited
           next
           #t)

          (vector-set!
           depth
           next
           (+ 1
              (vector-ref depth node)))

          (vector-set!
           (vector-ref up 0)
           next
           node)

          (vector-set!
           queue
           tail
           next)

          (set! tail (+ tail 1))))

      (bfs)))

  ;; Built binary lifting table.
  (for ([k (in-range 1 LOG)])

    (for ([node (in-range 1 (+ n 1))])

      (vector-set!
       (vector-ref up k)
       node
       (vector-ref
        (vector-ref up (- k 1))
        (vector-ref
         (vector-ref up (- k 1))
         node)))))

  ;; Precomputed powers of two modulo MOD.
  (define pow2
    (make-vector (+ n 1) 1))

  (for ([i (in-range 1 (+ n 1))])

    (vector-set!
     pow2
     i
     (remainder
      (* 2
         (vector-ref pow2 (- i 1)))
      MOD)))

  ;; Used binary lifting to find LCA.
  (define (lca a0 b0)

    (define a a0)
    (define b b0)

    (when (< (vector-ref depth a)
             (vector-ref depth b))
      (let ([tmp a])
        (set! a b)
        (set! b tmp)))

    (define diff
      (- (vector-ref depth a)
         (vector-ref depth b)))

    ;; Lifted deeper node.
    (for ([k (in-range LOG)])

      (when
          (not
           (zero?
            (bitwise-and
             diff
             (arithmetic-shift 1 k))))

        (set!
         a
         (vector-ref
          (vector-ref up k)
          a))))

    (if (= a b)

        a

        (begin

          ;; Lifted both nodes together.
          (for ([k (in-range (- LOG 1) -1 -1)])

            (when
                (not
                 (=
                  (vector-ref
                   (vector-ref up k)
                   a)

                  (vector-ref
                   (vector-ref up k)
                   b)))

              (set!
               a
               (vector-ref
                (vector-ref up k)
                a))

              (set!
               b
               (vector-ref
                (vector-ref up k)
                b))))

          (vector-ref
           (vector-ref up 0)
           a))))

  ;; Processed all queries.
  (for/list ([q queries])

    (define u (first q))
    (define v (second q))

    ;; Found lowest common ancestor.
    (define ancestor
      (lca u v))

    ;; Calculated distance.
    (define dist
      (- (+ (vector-ref depth u)
            (vector-ref depth v))
         (* 2
            (vector-ref
             depth
             ancestor))))

    ;; Empty path has no valid assignments.
    (if (= dist 0)

        0

        ;; Answer equals 2^(distance - 1).
        (vector-ref
         pow2
         (- dist 1)))))
